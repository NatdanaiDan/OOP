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


class Tasknormal:
    def __init__(self):
        self._task_list = []


class Taskfinished:
    def __init__(self):
        self._task_list = []


class Taskhighlight:
    def __init__(self):
        self._task_list = []


class Taskdeleted:
    def __init__(self):
        self._task_list = []


class List:
    def __init__(self, title):
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

    def add_task(self, task):
        self._task_normal.add_task(task)
