import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file if it exists
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()

app = Flask(__name__)

# Email configurations
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")  # App Password

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400
        
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        message = data.get("message", "").strip()

        if not name or not email or not message:
            return jsonify({"status": "error", "message": "All fields are required"}), 400

        # Create email message
        msg = MIMEMultipart("alternative")
        msg["From"] = SMTP_USER
        msg["To"] = SMTP_USER
        msg["Subject"] = f"New Client/Project Incoming from {name}"

        # Plain text fallback
        text_body = f"""You have received a new client inquiry and potential project incoming from the Shanti AI Showcase website.

Name: {name}
Email: {email}
Message:
{message}
"""

        # HTML formatted email body matching branding of Shanti AI
        formatted_message = message.replace("\n", "<br>")
        html_body = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>New Client / Project Incoming</title>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-color: #020208;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}
    .email-container {{
      max-width: 600px;
      margin: 40px auto;
      background-color: #0a0b10;
      border: 1px solid #1e1e2e;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }}
    .header {{
      background: #020208 linear-gradient(135deg, #020208 0%, #0c0d19 100%);
      padding: 30px;
      text-align: center;
      border-bottom: 1px solid #1e1e2e;
    }}
    .logo-container {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }}
    .logo-text {{
      font-family: 'Space Grotesk', -apple-system, sans-serif;
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.5px;
    }}
    .logo-glow {{
      color: #06b6d4;
    }}
    .content {{
      padding: 40px 30px;
      color: #f3f4f6;
    }}
    .badge {{
      display: inline-block;
      background: rgba(99, 102, 241, 0.1);
      border: 1px solid rgba(99, 102, 241, 0.3);
      padding: 6px 14px;
      border-radius: 50px;
      color: #818cf8;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 24px;
    }}
    .heading {{
      font-family: 'Space Grotesk', -apple-system, sans-serif;
      font-size: 22px;
      font-weight: 700;
      margin: 0 0 16px 0;
      color: #ffffff;
    }}
    .lead-text {{
      font-size: 15px;
      color: #9ca3af;
      line-height: 1.6;
      margin: 0 0 30px 0;
    }}
    .info-card {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid #1e1e2e;
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 30px;
    }}
    .info-row {{
      margin-bottom: 20px;
    }}
    .info-row:last-child {{
      margin-bottom: 0;
    }}
    .info-label {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #9ca3af;
      margin-bottom: 6px;
    }}
    .info-value {{
      font-size: 15px;
      color: #ffffff;
      font-weight: 600;
    }}
    .info-value a {{
      color: #06b6d4;
      text-decoration: none;
    }}
    .message-box {{
      background: rgba(99, 102, 241, 0.04);
      border-left: 3px solid #6366f1;
      padding: 20px;
      border-radius: 4px 12px 12px 4px;
      margin-top: 8px;
    }}
    .message-text {{
      font-size: 14px;
      color: #e5e7eb;
      line-height: 1.7;
      margin: 0;
    }}
    .button-container {{
      text-align: center;
      margin: 35px 0 10px 0;
    }}
    .btn {{
      display: inline-block;
      background: #6366f1 linear-gradient(135deg, #6366f1 0%, #d946ef 100%);
      color: #ffffff !important;
      padding: 14px 32px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      font-size: 14px;
      box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }}
    .footer {{
      background-color: #05060a;
      padding: 25px 30px;
      text-align: center;
      border-top: 1px solid #1e1e2e;
    }}
    .footer-text {{
      font-size: 12px;
      color: #6b7280;
      line-height: 1.5;
      margin: 0;
    }}
    .footer-text a {{
      color: #9ca3af;
      text-decoration: none;
    }}
  </style>
</head>
<body style="font-family: 'Plus Jakarta Sans', 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #020208; margin: 0; padding: 0; -webkit-font-smoothing: antialiased;">
  <div class="email-container" style="max-width: 600px; margin: 40px auto; background-color: #0a0b10; border: 1px solid #1e1e2e; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);">
    <div class="header" style="background: #020208 linear-gradient(135deg, #020208 0%, #0c0d19 100%); padding: 30px; text-align: center; border-bottom: 1px solid #1e1e2e;">
      <div class="logo-container" style="display: inline-flex; align-items: center; gap: 10px;">
        <img src="https://www.image.shantiinfosoft.com/images/shanti-small-light.png" alt="Shanti AI Logo" style="height: 28px; width: auto; vertical-align: middle;">
        <span class="logo-text" style="font-family: 'Space Grotesk', -apple-system, sans-serif; font-size: 24px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">Shanti <span class="logo-glow" style="color: #06b6d4;">AI</span></span>
      </div>
    </div>
    <div class="content" style="padding: 40px 30px; color: #f3f4f6;">
      <span class="badge" style="display: inline-block; background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); padding: 6px 14px; border-radius: 50px; color: #818cf8; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 24px;">New Client / Project Incoming</span>
      <p class="lead-text" style="font-size: 15px; color: #9ca3af; line-height: 1.6; margin: 0 0 30px 0;">A potential client has reached out to you regarding a potential project. Here are the incoming details:</p>
      
      <div class="info-card" style="background: rgba(255, 255, 255, 0.02); border: 1px solid #1e1e2e; border-radius: 12px; padding: 24px; margin-bottom: 30px;">
        <div class="info-row" style="margin-bottom: 20px;">
          <div class="info-label" style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #9ca3af; margin-bottom: 6px;">Sender Name</div>
          <div class="info-value" style="font-size: 15px; color: #ffffff; font-weight: 600;">{name}</div>
        </div>
        <div class="info-row" style="margin-bottom: 20px;">
          <div class="info-label" style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #9ca3af; margin-bottom: 6px;">Email Address</div>
          <div class="info-value" style="font-size: 15px; color: #ffffff; font-weight: 600;"><a href="mailto:{email}" style="color: #06b6d4; text-decoration: none;">{email}</a></div>
        </div>
        <div class="info-row" style="margin-bottom: 0;">
          <div class="info-label" style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #9ca3af; margin-bottom: 6px;">Client Message</div>
          <div class="message-box" style="background: rgba(99, 102, 241, 0.04); border-left: 3px solid #6366f1; padding: 20px; border-radius: 4px 12px 12px 4px; margin-top: 8px;">
            <p class="message-text" style="font-size: 14px; color: #e5e7eb; line-height: 1.7; margin: 0;">{formatted_message}</p>
          </div>
        </div>
      </div>
      
      <div class="button-container" style="text-align: center; margin: 35px 0 10px 0;">
        <a href="mailto:{email}" class="btn" style="display: inline-block; background: #6366f1 linear-gradient(135deg, #6366f1 0%, #d946ef 100%); color: #ffffff !important; padding: 14px 32px; border-radius: 50px; text-decoration: none; font-weight: 600; font-size: 14px; box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);">Reply via Email</a>
      </div>
    </div>
    <div class="footer" style="background-color: #05060a; padding: 25px 30px; text-align: center; border-top: 1px solid #1e1e2e;">
      <p class="footer-text" style="font-size: 12px; color: #6b7280; line-height: 1.5; margin: 0;">
        This notification was auto-generated by the <a href="https://ai-projects-display.vercel.app/" style="color: #9ca3af; text-decoration: none;">Shanti AI Showcase</a> platform.
      </p>
      <p class="footer-text" style="font-size: 12px; color: #6b7280; line-height: 1.5; margin: 8px 0 0 0;">
        © 2026 Shanti Infosoft. All rights reserved.
      </p>
    </div>
  </div>
</body>
</html>
"""

        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        # Send email
        if SMTP_PASSWORD:
            try:
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_USER, SMTP_USER, msg.as_string())
                server.quit()
                print(f"Email successfully sent to {SMTP_USER} via SMTP.")
            except Exception as e:
                print(f"SMTP Error: {e}")
                return jsonify({"status": "error", "message": f"SMTP Error: {str(e)}"}), 500
        else:
            # Fallback for development if no password configured
            print("\n" + "="*50)
            print("DEVELOPMENT MODE: No SMTP password configured.")
            print(f"Email would be sent to: {SMTP_USER}")
            print(f"Subject: {msg['Subject']}")
            print(f"Body:\n{text_body}")
            print("="*50 + "\n")

        return jsonify({"status": "success", "message": "Message received and logged successfully!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
