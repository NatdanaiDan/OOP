class User:
    def __init__(self):
        self._user_list = []

    def create_list(self, title):
        self._user_list.append(List(title))

    def get_list(self, list_id):
        for list in self._user_list:
            if list.id == list_id:
                return list

    def edit_tasklist_name(self, title, list_id):
        list_return = self.get_list(list_id)
        list_return.title = title

    def add_task(self, name, list_id):
        list_return = self.get_list(list_id)
        list_return.add_task(name)

    def edit_task_name(self, name, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.edit_task_name(name, task_id)

    def edit_task_description(self, description, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.edit_task_description(description, task_id)

    def edit_task_date(self, date, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.edit_task_date(date, task_id)

    def move_to_task_delete(self, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.move_to_task_delete(task_id)

    def move_to_task_finish(self, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.move_to_task_finish(task_id)

    def move_to_task_normal(self, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.move_to_task_normal(task_id)

    def move_to_task_highlight(self, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.move_to_task_highlight(task_id)

    def add_subtask(self, name, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.add_subtask(name, task_id)

    def edit_subtask_detail(self, name, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.edit_subtask_detail(name, task_id, subtask_id)

    def edit_subtask_status(self, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.edit_subtask_status(task_id, subtask_id)

    def remove_subtask(self, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.remove_subtask(task_id, subtask_id)

    @property
    def user_list(self):
        return self._user_list


class Subtask:
    id_subtask = 1

    def __init__(self, details):
        self._id = Subtask.id_subtask
        self._details = details
        self._status_completed = False
        Subtask.id_subtask += 1

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def id(self):
        return self._id

    @property
    def status_completed(self):
        return self._status_completed

    def change_status(self):
        self._status_completed = not self._status_completed


class Task:
    task_id = 1

    def __init__(self, name):
        self._id = Task.task_id
        self._name = name
        self._subtasks = []
        self._description = ""
        self._due_date = None
        self._status = "Normal"
        Task.task_id += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def subtasks(self):
        return self._subtasks

    @property
    def id(self):
        return self._id

    def get_subtask(self, subtask_id):
        for subtask in self._subtasks:
            if subtask.id == subtask_id:
                return subtask

    def add_subtask(self, detail):
        self._subtasks.append(Subtask(detail))

    def remove_subtask(self, subtask_id):
        for subtask in self._subtasks:
            if subtask.id == subtask_id:
                self._subtasks.remove(subtask)

    def edit_subtask_detail(self, detail, subtask_id):
        subtask = self.get_subtask(subtask_id)
        subtask.details = detail

    def edit_subtask_status(self, subtask_id):
        subtask = self.get_subtask(subtask_id)
        subtask.change_status()


class Bucket:
    def __init__(self):
        self._task_list = []

    def remove_task(self, task):
        self.task_list.remove(task)

    @property
    def task_list(self):
        return self._task_list


class Tasknormal(Bucket):
    pass


class Taskfinished(Bucket):
    pass


class Taskhighlight(Bucket):
    pass


class Taskdeleted(Bucket):
    pass


class Movetask:
    def get_where(self, task):
        where = task.status
        if where == "Normal":
            self.task_normal.remove_task(task)
        elif where == "Highlight":
            self.task_highlight.remove_task(task)
        elif where == "Finished":
            self.task_finished.remove_task(task)
        elif where == "Deleted":
            self.task_deleted.remove_task(task)

    def move_to_task_delete(self, task):
        self.get_where(task)
        task.status = "Deleted"
        self._task_deleted.task_list.append(task)

    def move_to_task_finish(self, task):
        self.get_where(task)
        task.status = "Finished"
        self._task_finished.task_list.append(task)

    def move_to_task_highlight(self, task):
        self.get_where(task)
        task.status = "Highlight"
        self._task_highlight.task_list.append(task)

    def move_to_task_normal(self, task):
        self.get_where(task)
        task.status = "Normal"
        self._task_normal.task_list.append(task)


class List(Movetask):
    id_list = 1

    def __init__(self, title):
        self._id = List.id_list
        self._title = title
        self._task_normal = Tasknormal()
        self._task_finished = Taskfinished()
        self._task_highlight = Taskhighlight()
        self._task_deleted = Taskdeleted()
        List.id_list += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def task_normal(self):
        return self._task_normal

    @property
    def task_finished(self):
        return self._task_finished

    @property
    def task_highlight(self):
        return self._task_highlight

    @property
    def task_deleted(self):
        return self._task_deleted

    @property
    def id(self):
        return self._id

    def get_task(self, task_id):
        for task in (
            self.task_normal.task_list
            + self.task_finished.task_list
            + self.task_highlight.task_list
            + self.task_deleted.task_list
        ):
            if task.id == task_id:
                return task

    def add_task(self, name):
        self.task_normal.task_list.append(Task(name))

    def edit_task_name(self, name, task_id):
        task = self.get_task(task_id)
        task.name = name

    def edit_task_description(self, description, task_id):
        task = self.get_task(task_id)
        task.description = description

    def edit_task_date(self, due_date, task_id):
        task = self.get_task(task_id)
        task.due_date = due_date

    def move_to_task_delete(self, task_id):
        task = self.get_task(task_id)
        super().move_to_task_delete(task)

    def move_to_task_finish(self, task_id):
        task = self.get_task(task_id)
        super().move_to_task_finish(task)

    def move_to_task_highlight(self, task_id):
        task = self.get_task(task_id)
        super().move_to_task_highlight(task)

    def move_to_task_normal(self, task_id):
        task = self.get_task(task_id)
        super().move_to_task_normal(task)

    def add_subtask(self, detail, task_id):
        task = self.get_task(task_id)
        task.add_subtask(detail)

    def edit_subtask_detail(self, detail, subtask_id, task_id):
        task = self.get_task(task_id)
        task.edit_subtask_detail(detail, subtask_id)

    def edit_subtask_status(self, subtask_id, task_id):
        task = self.get_task(task_id)
        task.edit_subtask_status(subtask_id)

    def remove_subtask(self, subtask_id, task_id):
        task = self.get_task(task_id)
        task.remove_subtask(subtask_id)


if __name__ == "__main__":
    import json
    from json import JSONEncoder

    class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

    user1 = User()
    user1.create_list("list1")
    user1.edit_tasklist_name("test", 1)
    employeeJSONData = json.dumps(user1, indent=4, cls=EmployeeEncoder)
    print(employeeJSONData)

    # studentObject = jsonpickle.decode(employeeJSONData)
    # print("Object type is: ", type(studentObject))
    # studentObject.create_list("list2")
    # print(studentObject.user_list)
