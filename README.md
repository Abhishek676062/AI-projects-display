<p align="center">
<img src="./assets/banner.png" width="100%">
</p>

<p align="center">
  <strong>An elite portfolio platform demonstrating cutting-edge AI Agent systems, speech recognition, computer vision, and workflow automation.</strong>
</p>

<p align="center">
  <a href="https://github.com/Shanti-Infosoft/AI-projects-display/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Shanti-Infosoft/AI-projects-display?style=for-the-badge&color=818cf8" alt="License Badge">
  </a>
  <a href="https://github.com/Shanti-Infosoft/AI-projects-display/releases">
    <img src="https://img.shields.io/github/v/release/Shanti-Infosoft/AI-projects-display?style=for-the-badge&color=a855f7" alt="Version Badge">
  </a>
  <img src="https://img.shields.io/badge/AI--Powered-True-ac0865?style=for-the-badge" alt="AI-Powered Badge">
  <img src="https://img.shields.io/badge/Open--Source-Yes-10b981?style=for-the-badge" alt="Open Source Badge">
</p>

<p align="center">
  <a href="#installation">Live Demo</a> •
  <a href="#project-structure">Documentation</a> •
  <a href="https://github.com/Shanti-Infosoft/AI-projects-display/issues">Report Issue</a>
</p>

---

## 📖 Overview

The **Shanti AI Showcase** is a responsive, highly-optimized web platform powered by Flask. It is engineered to highlight Shanti Infosoft's state-of-the-art implementations in Artificial Intelligence, including autonomous agents, advanced identity validation, speech intelligence, and secure cloud workflows. Featuring a premium dark-mode UI with smooth scroll animations, glassmorphism, and live interactive video demos.

---

## 🎨 System Architecture

This diagram displays the cloud architecture flow and routing from the user visiting the showcase down to experiencing the integrated AI models.

<p align="center">
<img src="./assets/architecture.png" width="100%">
</p>

---

## ⚡ Core Workflow

The end-to-end request lifecycle and validation pipeline showing how data flows between our automated modules.

<p align="center">
<img src="./assets/workflow.png" width="100%">
</p>

---

## 🌟 Key Features

| Capability | Description | Core Focus |
| :--- | :--- | :--- |
| **Agentic AI & MCP** | Deploy autonomous AI agents using Model Context Protocol (MCP) to securely execute tool actions. | System Extensibility |
| **Generative AI & LLMs** | Custom fine-tuned Large Language Models aligned directly with brand identities. | Text & Asset Generation |
| **Enterprise RAG** | High-performance Retrieval-Augmented Generation for company wikis & private datasets. | Knowledge Retrieval |
| **Conversational Voice AI** | Human-like voice agents managing bookings, customer service, and real-time requests. | Speech-to-Text & TTS |
| **Computer Vision Security** | Facial comparison and deepfake anti-spoofing liveness detection. | Anti-Spoofing / Identity |
| **Workflow Automation** | End-to-end automation of social media growth, VIP access controls, and repetitive tasks. | Growth & Efficiency |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Jinja2 Templates, HTML5, Vanilla CSS3, Javascript | Core interface, styling, scroll reveal animations |
| **Backend** | Flask (Python 3.10+) | Lightweight serving, routing, and environment config |
| **Server/WSGI** | Gunicorn | Production-grade WSGI HTTP Server |
| **Media Streaming** | Loom, Google Drive Embed APIs | Low-latency presentation delivery |
| **Infrastructure** | Render IaC (`render.yaml`) | Continuous Deployment |

---

## 📁 Project Structure

```bash
AI-projects-display/
├── assets/
│   ├── banner.png        # Repository hero banner
│   ├── architecture.png  # Platform system architecture
│   └── workflow.png      # AI processing workflow graphic
├── app.py                # Flask Application Entrypoint
├── render.yaml           # Render Infrastructure-as-Code Configuration
├── requirements.txt      # Python Packages
├── templates/
│   └── index.html        # Premium Glassmorphism UI (35KB)
└── README.md             # Project Documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.10 or higher
* Git

### Step-by-Step Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shanti-Infosoft/AI-projects-display.git
   cd AI-projects-display
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   python app.py
   ```
   The local development server will start at `http://127.0.0.1:5000/`.

---

## 🔑 Environment Variables

The core showcase dashboard runs out-of-the-box without keys, but individual integrated services depend on the following configurations:

| Variable | Description | Default / Required |
| :--- | :--- | :--- |
| `FLASK_ENV` | Environment mode (development/production) | `development` |
| `PORT` | Listening port for web server | `5000` |
| `OPENAI_API_KEY` | Required for LLM reasoning in Voice Agent & RAG assistant. | *Required for AI features* |
| `TELEGRAM_BOT_TOKEN` | Required for secure VIP photo link delivery. | *Required for Telegram bot* |
| `INSTAGRAM_USERNAME` | Automated profile username. | *Required for IG bot* |
| `INSTAGRAM_PASSWORD` | Automated profile password. | *Required for IG bot* |

---

## 🔌 API Endpoints

The web application exposes a simple, lightweight routing structure:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Renders the primary portfolio interface with all featured projects and interactive elements. |

---

## 📸 Screenshots

### Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Capabilities Overview
![Analytics](docs/screenshots/analytics.png)

### Video Demonstrations
![AI](docs/screenshots/ai.png)

---

## 🌍 Cloud Deployment

The repository includes native support for Render deployment via `render.yaml`. 

### Deploying to Render
1. Connect your GitHub repository to Render.
2. Select **Web Service**.
3. Render will auto-detect the `render.yaml` file, executing the following configurations:
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app`

---

## 🗺️ Roadmap

- [x] Responsive Showcase Dashboard
- [x] Glassmorphism Dark Theme UI
- [x] Multi-format Video Embed Integration (Loom, Google Drive)
- [x] Render Infrastructure-as-Code Configuration
- [ ] Direct Live Chat Widget for consultations
- [ ] Dynamically managed portfolio dashboard (Admin Panel)
- [ ] Analytics tracking for project click-throughs

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository.
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the branch (`git push origin feature/AmazingFeature`).
5. **Open** a Pull Request.

---

<p align="center">
  Built with ❤️ by <strong>Shanti Infosoft</strong>
</p>

<p align="center">
  🚀 AI Solutions • 🤖 Automation • ⚡ Scalable Products • 🌍 Global Innovation
</p>
