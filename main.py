from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from decouple import config
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils import Db
from .utils.Validations_Data import correct_user

app = FastAPI()


@app.post('/')
async def main(Request):
    pass


@app.get('/message')
async def message(request: Request):
    pass


@app.get('/message/{tab}')
async def message(request: Request):
    pass


@app.get('/message/{tab}/{message_id}')
async def message(request: Request):
    pass


@app.post('/search')
async def search(request: Request):
    pass
