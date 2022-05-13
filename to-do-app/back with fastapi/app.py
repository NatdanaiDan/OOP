from fastapi import FastAPI
from fastapi.responses import JSONResponse
import back
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


user1 = back.User()


@app.get("/get_data")
def get_data():
    return JSONResponse(content=jsonable_encoder(user1))


@app.get("/get_tasklist")
def get_tasklist(list_id: int):
    jsonlist = user1.get_list(list_id)
    return JSONResponse(content=jsonable_encoder(jsonlist))


@app.get("/get_subtask")
def get_subtask(list_id: int, task_id: int):
    list = user1.get_list(list_id)
    jsontask = list.get_task(task_id)
    return JSONResponse(content=jsonable_encoder(jsontask))


@app.get("/")
def read_root():
    return "Connected to the server"


### List


@app.get("/createlist")
def add_list(name: str):
    user1.create_list(name)


@app.get("/edittasklistname")
def edit_tasklist_name(name: str, list_id: int):
    user1.edit_tasklist_name(name, list_id)


### Task


@app.get("/addtask")
def add_task(name: str, list_id: int):
    user1.add_task(name, list_id)


@app.get("/edittask")
def edit_subtask(name: str, date: str, description: str, list_id: int, task_id: int):
    user1.edit_task(name, date, description, list_id, task_id)


@app.get("/move_to_task")
def move_to_task(list_id: int, task_id: int, destination: str):
    user1.move_to_task(list_id, task_id, destination)


### Subtask


@app.get("/addsubtask")
def add_subtask(name: str, list_id: int, task_id: int):
    user1.add_subtask(name, list_id, task_id)


@app.get("/editsubtaskdetail")
def edit_subtask_detail(name: str, list_id: int, task_id: int, subtask_id: int):
    user1.edit_subtask_detail(name, list_id, task_id, subtask_id)


@app.get("/editsubtaskstatus")
def edit_subtask_status(list_id: int, task_id: int, subtask_id: int):
    user1.edit_subtask_status(list_id, task_id, subtask_id)
