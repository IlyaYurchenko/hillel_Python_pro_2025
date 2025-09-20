from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import random
import os
import string
import json, aiofiles
import motor.motor_asyncio
from pymongo import MongoClient


app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name="static")
templates = Jinja2Templates(directory="templates")
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
db_client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://admin:password@{mongo_host}:27017')
db = db_client.fastAPI
url_collection = db.urls

    
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse( 
        request=request, 
        name="index.html")

@app.get('/{short_url}')
async def short_url_handler(short_url: str):
    urls_data = await url_collection.find_one({'short_url': short_url})
    return RedirectResponse(urls_data.get('url')) if urls_data else {"error": "Short URL not found"}

@app.post("/")
async def create_url(url: Annotated[str, Form()]):
    
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(chars, k=6))
    
    await url_collection.insert_one({'short_url': short_url, 'url': url})
   
    return {"short_url": short_url, "\nurl": url}