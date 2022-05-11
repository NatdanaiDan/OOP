from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import back

app = FastAPI()


templates = Jinja2Templates(directory="templates")
user1 = back.User()


@app.get("/index/", response_class=HTMLResponse)
def movielist(request: Request):
    user_list = user1.user_list
    context = {"request": request, "user_list": user_list}
    return templates.TemplateResponse("index.html", context)
