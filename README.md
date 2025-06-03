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
```

### 2. Create .env file

```bash
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/webhooks?retryWrites=true&w=majority
```

### 3. Install dependencies

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python run.py
```
It will start at: http://localhost:5000

### 5. Start ngrok to expose the Flask server

```bash
ngrok http 5000
```

### 6. Set up GitHub Webhook

<ul> Go to your GitHub repo:</ul>

<li>Settings → Webhooks → Add webhook<li/>
<li>Payload URL:</li>

```bash
https://abc123.ngrok.io/webhook/receiver
```

<li>Content type: application/json</li>
<li>Events: Choose:</li>
<li>Push events</li>
<li>Pull requests</li>

Click Add Webhook

### Project Structure

```bash
webhook-repo/
├── app/
│   ├── static/script.js
│   ├── templates/index.html
│   ├── webhook/routes.py
│   ├── extensions.py
│   └── __init__.py
├── .env
├── run.py
├── requirements.txt
└── README.md
```

### Sample Output

```bash
"Soham" pushed to "main" on 3rd June 2025 - 9:00 PM UTC  
"Soham" submitted a pull request from "dev" to "main" on 3rd June 2025 - 8:55 PM UTC  
```

