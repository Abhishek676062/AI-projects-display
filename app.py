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
RECIPIENT_EMAIL = "manjesh.shantiinfosoft@gmail.com"
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "manjesh.shantiinfosoft@gmail.com")
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
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = f"New AI Project Brief from {name}"

        body = f"""You have received a new project brief submission from the Shanti AI Showcase website.

Name: {name}
Email: {email}
Message:
{message}
"""
        msg.attach(MIMEText(body, "plain"))

        # Send email
        if SMTP_PASSWORD:
            try:
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_USER, RECIPIENT_EMAIL, msg.as_string())
                server.quit()
                print(f"Email successfully sent to {RECIPIENT_EMAIL} via SMTP.")
            except Exception as e:
                print(f"SMTP Error: {e}")
                return jsonify({"status": "error", "message": f"SMTP Error: {str(e)}"}), 500
        else:
            # Fallback for development if no password configured
            print("\n" + "="*50)
            print("DEVELOPMENT MODE: No SMTP password configured.")
            print(f"Email would be sent to: {RECIPIENT_EMAIL}")
            print(f"Subject: {msg['Subject']}")
            print(f"Body:\n{body}")
            print("="*50 + "\n")

        return jsonify({"status": "success", "message": "Message received and logged successfully!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
