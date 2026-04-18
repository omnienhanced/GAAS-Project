from fastapi import APIRouter
from pydantic import BaseModel
from app.worker.executor import run_code
from fastapi.responses import FileResponse
import os

router = APIRouter()


# 📌 Request model
class CodeRequest(BaseModel):
    code: str


# 🚀 1. Run user code
@router.post("/submit-job")
def submit_job(req: CodeRequest):
    return run_code(req.code)


# 📥 2. Download trained model
@router.get("/download-model")
def download_model():
    file_path = "scripts/model.pkl"

    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename="model.pkl",
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": "attachment; filename=model.pkl"
            }
        )
    else:
        return {"error": "Model not found"}


# 📊 3. Server status (optional but useful)
@router.get("/status")
def status():
    return {
        "server": "running",
        "mode": "CPU",
        "docker": "active"
    }


# 📄 4. Last executed code (optional)
@router.get("/last-code")
def last_code():
    try:
        with open("scripts/user_script.py", "r") as f:
            return {"last_code": f.read()}
    except:
        return {"error": "No code found"}