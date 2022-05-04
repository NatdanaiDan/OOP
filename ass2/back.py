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


class File:
    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return self._path


class SoundFile(File):
    def __init__(self, path):
        super().__init__(path)


class ImageFile(File):
    def __init__(self, path):
        super().__init__(path)


class DocumentFile(File):
    def __init__(self, path):
        super().__init__(path)


class Task:
    def __init__(self, name):
        self._name = name
        self._subtasks = []
        self._file = []
        self._description = ""
        self._due_date = None

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
    def move_to_task_deleted(self, task):
        self._task_deleted.task_list.append(task)

    def move_to_task_finished(self, task):
        self._task_finished.task_list.append(task)

    def move_to_task_highlight(self, task):
        self._task_highlight.task_list.append(task)

    def move_to_task_normal(self, task):
        self._task_normal.task_list.append(task)


"""
เดี่ยวมา หาวิธีเอาออกจาก list ตัวเอง
"""


class List(Movetask):
    def __init__(self, title):
        self._dict
        self._tile = title
        self._task_normal = Tasknormal()
        self._task_finished = Taskfinished()
        self._task_highlight = Taskhighlight()
        self._task_deleted = Taskdeleted()

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

    def add_task(self, name):
        self.task_normal.task_list.append(Task(name))


list1 = List("list1")
list1.add_task("task1")
list1.add_task("task2")
x = list1.task_normal.task_list[0]
list1.move_to_task_deleted(x)
import json
from json import JSONEncoder


class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


employeeJSONData = json.dumps(list1, indent=4, cls=EmployeeEncoder)
print(employeeJSONData)
