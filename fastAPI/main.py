from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import random
import string
import json, aiofiles


app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse( 
        request=request, 
        name="index.html")

@app.get('/{short_url}')
async def short_url_handler(short_url: str):
    async with aiofiles.open('urls.json', mode='r') as f:
        urls_data = json.loads(await f.read())
    return RedirectResponse(urls_data.get(short_url))

@app.post("/")
async def create_url(url: Annotated[str, Form()]):
    
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(chars, k=6))
    
    async with aiofiles.open('urls.json', mode='r') as f:
        urls_data = json.loads(await f.read())
    
    urls_data[short_url] = url
    
    async with aiofiles.open('urls.json', mode='w') as f:
            await f.write(json.dumps(urls_data, indent=4))
    return {"short_link": short_url, "url": url}