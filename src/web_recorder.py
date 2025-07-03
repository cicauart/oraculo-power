"""Pequeño servidor FastAPI para grabar audio desde el navegador."""
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from pathlib import Path
import time
import uvicorn

APP = FastAPI()
UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)

@APP.get("/", response_class=HTMLResponse)
def index():
    with open(Path(__file__).parent / "templates" / "record.html", "r", encoding="utf-8") as f:
        return f.read()

@APP.post("/upload")
async def upload(file: UploadFile = File(...)):
    out = UPLOAD_DIR / f"record_{int(time.time())}.webm"
    with open(out, "wb") as f:
        f.write(await file.read())
    return {"message": "ok", "file": str(out)}

if __name__ == "__main__":
    uvicorn.run("src.web_recorder:APP", host="0.0.0.0", port=8000)
