from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import subprocess
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client["twitter_trends"]
collection = db["trending_topics"]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/run_script", response_class=HTMLResponse)
async def run_script(request: Request):
    subprocess.call(["python", "app/selenium_script.py"])
    record = collection.find().sort([("_id", -1)]).limit(1)[0]
    return templates.TemplateResponse(
        "results.html", {"request": request, "record": record}
    )
