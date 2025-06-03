# 🔔 GitHub Webhook Listener (Flask + MongoDB + ngrok)

This project listens to **GitHub webhooks** (e.g., `push`, `pull_request`, `merge`) and logs them to **MongoDB Atlas**. A minimal UI displays these events in real time, refreshing every 15 seconds.

---

## 📦 Tech Stack

- **Backend:** Python + Flask + Flask-PyMongo
- **Database:** MongoDB Atlas
- **Frontend:** HTML + JavaScript
- **Tunnel:** ngrok
- **Webhook Source:** GitHub

---

## 📸 Features

- Receives webhooks from GitHub
- Stores:
  - Event type: `push`, `pull_request`, `merge`
  - Author
  - Source & target branches
  - Timestamp (in UTC)
- Shows the latest events live on the frontend
- Polls every 15 seconds without refresh

---

## 🧑‍💻 Setup Instructions

### 🔧 1. Clone the repo

```bash
git clone https://github.com/your-username/webhook-repo.git
cd webhook-repo
