class User:
    def __init__(self):
        self._user_list = []

    def create_list(self, title):
        self._user_list.append(List(title))

    @property
    def user_list(self):
        return self._user_list


class Subtask:
    def __init__(self, details):
        self._details = details
        self._status_completed = False

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

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

    def add_subtask(self, detail):
        self._subtasks.append(Subtask(detail))

    def remove_subtask(self, detail):
        for subtask in self._subtasks:
            if subtask.details == detail:
                self._subtasks.remove(subtask)
                break


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

    def move_to_task_deleted(self, task):
        self.get_where(task)
        task.status = "Deleted"
        self._task_deleted.task_list.append(task)

    def move_to_task_finished(self, task):
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

    employeeJSONData = json.dumps(user1, indent=4, cls=EmployeeEncoder)
    print(employeeJSONData)
