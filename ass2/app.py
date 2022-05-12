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

# import jsonpickle
import json
from json import JSONEncoder


user1 = back.User()


class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def save_to_json(obj):
    with open("data.json", "w") as f:
        json.dump(obj, f, indent=4, cls=EmployeeEncoder)


@app.get("/get_data")
def get_data():
    f = open("data.json")
    data = json.load(f)
    f.close()
    return JSONResponse(content=data)


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
    save_to_json(user1)


@app.get("/edittasklistname")
def edit_tasklist_name(name: str, list_id: int):
    user1.edit_tasklist_name(name, list_id)
    save_to_json(user1)


### Task


@app.get("/addtask")
def add_task(name: str, list_id: int):
    user1.add_task(name, list_id)
    save_to_json(user1)


@app.get("/edittaskdate")
def edit_task_date(due_date: str, list_id: int, task_id: int):
    user1.edit_task_date(due_date, list_id, task_id)
    save_to_json(user1)


@app.get("/edittaskname")
def edit_task_name(name: str, list_id: int, task_id: int):
    user1.edit_task_name(name, list_id, task_id)
    save_to_json(user1)


@app.get("/edittaskdescription")
def edit_task_description(name: str, list_id: int, task_id: int):
    user1.edit_task_description(name, list_id, task_id)
    save_to_json(user1)


@app.get("/move_to_task_deleted")
def move_to_task_delete(list_id: int, task_id: int):
    user1.move_to_task_delete(list_id, task_id)
    save_to_json(user1)


@app.get("/move_to_task_finished")
def move_to_task_finish(list_id: int, task_id: int):
    user1.move_to_task_finish(list_id, task_id)
    save_to_json(user1)


@app.get("/move_to_task_normal")
def move_to_task_normal(list_id: int, task_id: int):
    user1.move_to_task_normal(list_id, task_id)
    save_to_json(user1)


@app.get("/move_to_task_highlight")
def move_to_task_highlight(list_id: int, task_id: int):
    user1.move_to_task_highlight(list_id, task_id)
    save_to_json(user1)


### Subtask


@app.get("/addsubtask")
def add_subtask(name: str, list_id: int, task_id: int):
    user1.add_subtask(name, list_id, task_id)
    save_to_json(user1)


@app.get("/editsubtaskdetail")
def edit_subtask_detail(name: str, list_id: int, task_id: int, subtask_id: int):
    user1.edit_subtask_detail(name, list_id, task_id, subtask_id)
    save_to_json(user1)


@app.get("/editsubtaskstatus")
def edit_subtask_status(list_id: int, task_id: int, subtask_id: int):
    user1.edit_subtask_status(list_id, task_id, subtask_id)
    save_to_json(user1)


@app.get("/removesubtask")
def remove_subtask(list_id: int, task_id: int, subtask_id: int):
    user1.remove_subtask(list_id, task_id, subtask_id)
    save_to_json(user1)


@app.get("/edittask")
def edit_subtask(name: str, date: str, description: str, list_id: int, task_id: int):
    user1.edit_task_name(name, list_id, task_id)
    user1.edit_task_date(date, list_id, task_id)
    user1.edit_task_description(description, list_id, task_id)
    save_to_json(user1)
