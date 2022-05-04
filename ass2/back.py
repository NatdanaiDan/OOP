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
        self._task_normal.task_list.append(Task(name))

    def delete_to_normal(self, task):
        self._task_normal.task_list.append(task)
        self._task_deleted.remove_task(task)

    def highlight_to_normal(self, task):
        self._task_normal.task_list.append(task)
        self._task_highlight.remove_task(task)

    def finished_to_normal(self, task):
        self._task_normal.task_list.append(task)
        self._task_finished.remove_task(task)

    def normal_to_highlight(self, task):
        self._task_highlight.task_list.append(task)
        self._task_normal.remove_task(task)

    def normal_to_finished(self, task):
        self._task_finished.task_list.append(task)
        self._task_normal.remove_task(task)

    def normal_to_deleted(self, task):
        self._task_deleted.task_list.append(task)
        self._task_normal.remove_task(task)


list1 = List("list1")
list1.add_task("task1")
list1.add_task("task2")
print(list1.task_normal.task_list)
