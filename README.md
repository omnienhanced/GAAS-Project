# 🚀 Cloud-Based Code Execution & ML Platform

<p align="center">
  <b>A Mini Cloud System to Execute Code & Train ML Models in Isolated Docker Containers</b>
</p>

---

## 🌟 Features

* 🧠 Remote Python Code Execution
* 🐳 Docker-based Isolated Environment
* ⚡ FastAPI Backend (High Performance)
* 🌐 Interactive Frontend UI
* 🤖 Machine Learning Support (Scikit-learn)
* 📥 Download Trained Models (`.pkl`)
* ⏱ Execution Time Tracking
* 🔐 Safe & Dependency-Free Execution

---

## 🏗️ Project Architecture

```text
User → Frontend UI → FastAPI Backend → Docker Container → Output → UI
```

---

## 📁 Project Structure

```text
gaas-project/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── worker/
│   │   └── executor.py
│
├── scripts/
│   └── user_script.py
│
├── frontend/
│   └── index.html
│
├── main.py
├── requirements.txt
└── Dockerfile
```

---

## ⚙️ Tech Stack

| Layer      | Technology                |
| ---------- | ------------------------- |
| Backend    | FastAPI                   |
| Execution  | Docker                    |
| Frontend   | HTML, CSS, JavaScript     |
| ML Support | Scikit-learn              |
| Deployment | Cloudflare Tunnel / Ngrok |

---

## 🚀 Getting Started

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/omnienhanced/gaas-project.git
cd gaas-project
```

---

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Build Docker Image

```bash
docker build -t gaas-image .
```

---

### 🔹 4. Run Backend Server

```bash
python -m uvicorn main:app --reload
```

---

### 🔹 5. Launch Frontend

Open:

```text
frontend/index.html
```

---

## 🌐 API Endpoints

| Endpoint          | Method | Description               |
| ----------------- | ------ | ------------------------- |
| `/submit-job`     | POST   | Execute user code         |
| `/download-model` | GET    | Download trained ML model |
| `/status`         | GET    | Server status             |
| `/last-code`      | GET    | Last executed code        |

---

## 🧪 Sample ML Test Code

```python
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

X = np.array([[1],[2],[3],[4]])
y = np.array([2,4,6,8])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved!")
```

---

## 🌍 Deployment Options

### 🔹 Local Network

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

---

### 🔹 Cloudflare Tunnel

```bash
cloudflared tunnel --url http://localhost:8000
```

---

### 🔹 Ngrok

```bash
ngrok http 8000
```

---

## 🧠 How It Works

1. User writes code in UI
2. Frontend sends request to backend
3. Backend stores code in script
4. Docker container executes code
5. Output returned to frontend
6. ML model saved & available for download

---

## 🔐 Advantages

* ✔ No dependency conflicts
* ✔ Secure container execution
* ✔ Supports ML workflows
* ✔ Easy-to-use interface
* ✔ Lightweight system

---

## ⚠️ Limitations

* ❌ Limited scalability (local deployment)
* ❌ Requires Docker installation
* ❌ Basic security (can be improved)

---

## 🚀 Future Enhancements

* 🔐 User Authentication
* 🌍 Full Cloud Deployment (AWS / Azure)
* 🧠 Multi-language Support
* ⚙️ Job Queue System
* 🎨 React-based UI

---

## 👨‍💻 Author

**omnienhanced**

💡 Project: Cloud Code Execution & ML Platform

---

## ⭐ Show Some Love

If you found this project useful, consider giving it a ⭐ on GitHub!
