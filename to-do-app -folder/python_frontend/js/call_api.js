function add_list(name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/createlist?name=" + name, true);
    xmlhttp.send();
}

function add_tasklist(event) {
    if (event.keyCode == 13) {
        let task_list_name = document.getElementById('task_list_name').value
        add_list(task_list_name)

        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                let task_data = JSON.parse(this.responseText)
                let task_list_dom = document.getElementById('todo_list')
                task_data['_user_list'].forEach(element => {
                    if (element['_title'] == task_list_name) {
                        task_list_dom.innerHTML += `<li class="li-list" onclick="get_task_in_tasklist(${element['_id']})">${element['_title']}</li>`
                    }
                });
                document.getElementById('task_list_name').value = " "
                return true;
            } else {
                return false;
            }
        };
        xmlhttp.open("GET", "http://127.0.0.1:8000/get_data", true);
        xmlhttp.send();
    }
}

function get_finish_task() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let task_data = JSON.parse(this.responseText)
            let task_todo_dom = document.getElementById('task_todo')
            task_todo_dom.innerHTML = ""
            document.getElementById('task_input').hidden = true
            document.getElementById('task_edit').hidden = true
            document.getElementById('title_task').innerHTML = "Finished Task"
            task_data['_user_list'].forEach(element => {
                let id_list = element['_id']
                element['_task_finished']['_task_list'].forEach(element => {
                    task_todo_dom.innerHTML += `
                    <li class="list-task task${id_list}todo${element['_id']}" id="todo_task">
                        <a href="#" onclick="revert_to_normal(${id_list}, ${element['_id']})"><div><img src="./img/undo.png" alt="" /></div></a>
                        <h1>${element['_name']}</h1>
                    </li>`
                })
            })
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/get_data", true);
    xmlhttp.send();
}

function get_delete_task() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let task_data = JSON.parse(this.responseText)
            let task_todo_dom = document.getElementById('task_todo')
            task_todo_dom.innerHTML = ""
            document.getElementById('task_input').hidden = true
            document.getElementById('task_edit').hidden = true
            document.getElementById('title_task').innerHTML = "Deleted Task"
            task_data['_user_list'].forEach(element => {
                let id_list = element['_id']
                element['_task_deleted']['_task_list'].forEach(element => {
                    task_todo_dom.innerHTML += `
                    <li class="list-task task${id_list}todo${element['_id']}" id="todo_task">
                        <a href="#" onclick="revert_to_normal(${id_list}, ${element['_id']})"><div><img src="./img/undo.png" alt="" /></div></a>
                        <h1>${element['_name']}</h1>
                    </li>`
                })
            })

            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/get_data", true);
    xmlhttp.send();
}

function get_task_in_tasklist(id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let task_data = JSON.parse(this.responseText)
            let task_todo_dom = document.getElementById('task_todo')
            task_todo_dom.innerHTML = ""
            document.getElementById('task_input').hidden = false
            document.getElementById('task_edit').hidden = true
            document.getElementById('title_task').innerHTML = task_data['_title']
            let id_list = task_data['_id']
            task_todo_dom.innerHTML += `<input type="hidden" id="id_list" name="${id_list}" value="${id_list}">`
            document.getElementById('task_input').value = ""
            task_data['_task_highlight']['_task_list'].forEach(element => {
                task_todo_dom.innerHTML += `
                <li class="list-task task${id_list}todo${element['_id']}" id="todo_task">
                    <a href="#" onclick="complete_task(${id_list}, ${element['_id']})"><div><img src="./img/check.png" alt="" /></div></a>
                    <h1>${element['_name']}</h1>
                    <a href="#" onclick="edit_task(${id_list}, ${element['_id']})">
                        <img class="pencil" src="./img/draw.png" alt="" />
                    </a>
                    <a href="#" onclick="delete_task(${id_list}, ${element['_id']})">
                        <img class="bin" src="./img/bin.png" alt="" />
                    </a>
                </li>`
            })

            task_data['_task_normal']['_task_list'].forEach(element => {
                task_todo_dom.innerHTML += `
                <li class="list-task task${id_list}todo${element['_id']}" id="todo_task">
                    <a href="#" onclick="complete_task(${id_list}, ${element['_id']})"><div><img src="./img/check.png" alt="" /></div></a>
                    <h1>${element['_name']}</h1>
                    <a href="#" onclick="edit_task(${id_list}, ${element['_id']})">
                        <img class="pencil" src="./img/draw.png" alt="" />
                    </a>
                    <a href="#" onclick="delete_task(${id_list}, ${element['_id']})">
                        <img class="bin" src="./img/bin.png" alt="" />
                    </a>
                </li>`
            })

            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/get_tasklist?list_id=" + id, true);
    xmlhttp.send();
}

function delete_task(id_list, id_task) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $(`.task${id_list}todo${id_task}`).remove()
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/move_to_task?destination=Deleted&list_id=" + id_list + "&task_id=" + id_task, true);
    xmlhttp.send();
}

function complete_task(id_list, id_task) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $(`.task${id_list}todo${id_task}`).remove()
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/move_to_task?destination=Finished&list_id=" + id_list + "&task_id=" + id_task, true);
    xmlhttp.send();
}

function revert_to_normal(id_list, id_task) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $(`.task${id_list}todo${id_task}`).remove()
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/move_to_task?destination=Normal&list_id=" + id_list + "&task_id=" + id_task, true);
    xmlhttp.send();
}

function add_task_in_task_list(event) {
    if (event.keyCode == 13) {
        let id_tasklist = document.getElementById('id_list').value
        let task_input = document.getElementById('task_input').value
        let task_todo_dom = document.getElementById('task_todo')

        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var xmlhttp = new XMLHttpRequest();
                xmlhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        let all_task_in_tasklist = JSON.parse(this.responseText);
                        all_task_in_tasklist['_task_normal']['_task_list'].reverse().forEach(element => {
                            if (element['_name'] == task_input) {
                                task_todo_dom.innerHTML += `
                                <li class="list-task task${id_tasklist}todo${element['_id']}" id="todo_task">
                                    <a href="#" onclick="complete_task(${id_tasklist}, ${element['_id']})"><div><img src="./img/check.png" alt="" /></div></a>
                                    <h1>${element['_name']}</h1>
                                    <a href="#" onclick="edit_task(${id_tasklist}, ${element['_id']})">
                                        <img class="pencil" src="./img/draw.png" alt="" />
                                    </a>
                                    <a href="#" onclick="delete_task(${id_tasklist}, ${element['_id']})">
                                        <img class="bin" src="./img/bin.png" alt="" />
                                    </a>
                                </li>`
                            }
                        })
                        document.getElementById('task_input').value = ""
                        return true;
                    } else {
                        return false;
                    }
                };
                xmlhttp.open("GET", "http://127.0.0.1:8000/get_tasklist?list_id=" + id_tasklist, true);
                xmlhttp.send();
                return true;
            } else {
                return false;
            }
        };
        xmlhttp.open("GET", "http://127.0.0.1:8000/addtask?name=" + task_input + "&list_id=" + id_tasklist, true);
        xmlhttp.send();
    }
}

function add_sub_task_to_task(event) {
    if (event.keyCode == 13) {
        let subtask_detail = document.getElementById('add_subtask').value
        let edit_list_id = document.getElementById('edit_list_id').value
        let edit_task_id = document.getElementById('edit_task_id').value

        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var xmlhttp = new XMLHttpRequest();
                xmlhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        let subtask_data = JSON.parse(this.responseText);
                        let edit_subtask_dom = document.getElementById('edit_subtask')
                        subtask_data['_subtasks'].reverse().forEach(element => {
                            if (subtask_detail == element['_details']) {
                                edit_subtask_dom.innerHTML += `
                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">⬛</span>
                        <input
                        class="form-control"
                        type="text"
                        placeholder="Type sub task (optional)"
                        name="data_subtask"
                        id="data_subtask${element['_id']}"
                        onkeyup="edit_subtask_in_task(${edit_list_id}, ${edit_task_id}, ${element['_id']}, event)"
                        value="${element['_details']}"
                        />
                        </div>
                        `
                            }

                        })

                        return true;
                    } else {
                        return false;
                    }
                };
                xmlhttp.open("GET", `http://127.0.0.1:8000/get_subtask?list_id=${edit_list_id}&task_id=${edit_task_id}`, true);
                xmlhttp.send();
                return true;
            } else {
                return false;
            }
        };
        xmlhttp.open("GET", `http://127.0.0.1:8000/addsubtask?name=${subtask_detail}&list_id=${edit_list_id}&task_id=${edit_task_id}`, true);
        xmlhttp.send();
    }
}

function save_task() {
    let list_id = document.getElementById('edit_list_id').value
    let task_id = document.getElementById('edit_task_id').value
    let task_name = document.getElementById('task_name').value
    let task_detail = document.getElementById('task_detail').value
    let datetime = document.getElementById('datepicker').value

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            get_task_in_tasklist(list_id)
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", `http://127.0.0.1:8000/edittask?name=${task_name}&date=${datetime}&description=${task_detail}&list_id=${list_id}&task_id=${task_id}`, true);
    xmlhttp.send();
}

function edit_subtask_in_task(id_list, id_task, id_subtask) {
    let subtask_data = document.getElementById(`data_subtask${id_subtask}`).value
    console.log(id_list, id_task, id_subtask);
    console.log(subtask_data);

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", `http://127.0.0.1:8000/editsubtaskdetail?name=${subtask_data}&list_id=${id_list}&task_id=${id_task}&subtask_id=${id_subtask}`, true);
    xmlhttp.send();
}

function set_highlight() {
    let list_id = document.getElementById('edit_list_id').value
    let task_id = document.getElementById('edit_task_id').value
    let status = document.getElementById('is_highlight').value
    save_task()
    if (status == "Normal") {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                get_task_in_tasklist(list_id)
                return true;
            } else {
                return false;
            }
        };
        xmlhttp.open("GET", `http://127.0.0.1:8000/move_to_task?destination=Highlight&list_id=${list_id}&task_id=${task_id}`, true);
        xmlhttp.send();
    } else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {

                get_task_in_tasklist(list_id)
                return true;
            } else {
                return false;
            }
        };
        xmlhttp.open("GET", `http://127.0.0.1:8000/move_to_task?destination=Normal&list_id=${list_id}&task_id=${task_id}`, true);
        xmlhttp.send();
    }


}

function edit_task(id_list, id_task) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let task_data = JSON.parse(this.responseText)
            let task_todo_dom = document.getElementById('task_todo')
            task_todo_dom.innerHTML = ""
            document.getElementById('title_task').innerHTML = task_data['_name']
            document.getElementById('task_input').hidden = true
            document.getElementById('task_edit').hidden = false

            document.getElementById('datepicker').value = task_data['_due_date']
            document.getElementById('edit_list_id').value = id_list
            document.getElementById('edit_task_id').value = id_task
            document.getElementById('task_name').value = task_data['_name']
            document.getElementById('task_detail').value = task_data['_description']
            document.getElementById('is_highlight').value = task_data['_status']
            console.log(task_data)
            if (task_data['_status'] == "Normal") {
                document.getElementById('star_highlight').hidden = true
            } else {
                document.getElementById('star_highlight').hidden = false
            }

            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    let subtask_data = JSON.parse(this.responseText);
                    let edit_subtask_dom = document.getElementById('edit_subtask')

                    edit_subtask_dom.innerHTML = ""
                    edit_subtask_dom.innerHTML += `
                <input
                class="form-control"
                type="text"
                placeholder="Type sub task (optional)"
                name="add_subtask"
                id="add_subtask"
                onkeypress="add_sub_task_to_task(event)"
                />
                `

                    subtask_data['_subtasks'].reverse().forEach(element => {
                        edit_subtask_dom.innerHTML += `
                    <div class="input-group mb-3">
                        <a href="#" onclick="check_subtask(${id_list}, ${id_task}, ${element['_id']})"><span class="input-group-text" id="basic-addon1">⬛</span></a>
                    <input
                    class="form-control input-group mb-3"
                    type="text"
                    placeholder="Type sub task (optional)"
                    name="data_subtask"
                    id="data_subtask${element['_id']}"
                    onkeyup="edit_subtask_in_task(${id_list}, ${id_task}, ${element['_id']}, event)"
                    value="${element['_details']}"
                    />
                    </div>
                    `
                    })

                    return true;
                } else {
                    return false;
                }
            };
            xmlhttp.open("GET", `http://127.0.0.1:8000/get_subtask?list_id=${id_list}&task_id=${id_task}`, true);
            xmlhttp.send();

            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/get_subtask?list_id=" + id_list + "&task_id=" + id_task, true);
    xmlhttp.send();
}

function main() {
    document.getElementById('title_task').innerHTML = "highlight task"

    document.getElementById('task_input').hidden = true
    document.getElementById('task_edit').hidden = true
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let task_data = JSON.parse(this.responseText)
            let task_list_dom = document.getElementById('todo_list')
            let task_todo_dom = document.getElementById('task_todo')
            task_list_dom.innerHTML = ""
            task_todo_dom.innerHTML = ""

            task_data['_user_list'].forEach(element => {
                task_list_dom.innerHTML += `<li class="li-list" onclick="get_task_in_tasklist(${element['_id']})">${element['_title']}</li>`
                element['_task_highlight']['_task_list'].forEach(element => {
                    task_todo_dom.innerHTML += `
                    <li class="list-task" id="todo_task">
                        <h1>${element['_name']}</h1>
                    </li>`
                })
            });
            return true;
        } else {
            return false;
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/get_data", true);
    xmlhttp.send();
}