from fastapi import FastAPI, Request, Form, status
from pydantic import BaseModel
from test import NotionAPISupport
from fastapi.templating import Jinja2Templates

# uvicorn main:app --reload -> uruchomienie

app = FastAPI()
api = NotionAPISupport()


class AddIdeA(BaseModel):
    Title: str
    Status: str
    Link_GitHub: str = None
    Description: str = None

@app.get("/")
async def root():
    return api.GetInformation()
