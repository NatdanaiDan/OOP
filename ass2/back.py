from superclass import All_command_front, TaskAction, SubtaskAction, Movetask


class User(All_command_front):
    def __init__(self):
        self._user_list = []

    def create_list(self, title):
        self._user_list.append(List(title))

    def get_list(self, list_id):
        for list in self._user_list:
            if list.id == list_id:
                return list

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


class Task(SubtaskAction):
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


class List(Movetask, TaskAction, SubtaskAction):
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
