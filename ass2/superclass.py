class All_command_front:
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
        list_return.edit_subtask_detail_signal(name, task_id, subtask_id)

    def edit_subtask_status(self, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.edit_subtask_status_signal(task_id, subtask_id)

    def remove_subtask(self, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.remove_subtask_signal(task_id, subtask_id)


class TaskAction:
    def edit_task_name(self, name, task_id):
        task = self.get_task(task_id)
        task.name = name

    def edit_task_description(self, description, task_id):
        task = self.get_task(task_id)
        task.description = description

    def edit_task_date(self, due_date, task_id):
        task = self.get_task(task_id)
        task.due_date = due_date


class SubtaskAction:
    def add_subtask(self, detail, task_id):
        task = self.get_task(task_id)
        task.add_subtask(detail)

    def edit_subtask_detail_signal(self, detail, subtask_id, task_id):
        task = self.get_task(task_id)
        task.edit_subtask_detail(detail, subtask_id)

    def edit_subtask_detail(self, detail, subtask_id):
        subtask = self.get_subtask(subtask_id)
        subtask.details = detail

    def edit_subtask_status_signal(self, subtask_id, task_id):
        task = self.get_task(task_id)
        task.edit_subtask_status(subtask_id)

    def edit_subtask_status(self, subtask_id):
        subtask = self.get_subtask(subtask_id)
        subtask.change_status()

    def remove_subtask_signal(self, subtask_id, task_id):
        task = self.get_task(task_id)
        task.remove_subtask(subtask_id)

    def remove_subtask(self, subtask_id):
        for subtask in self._subtasks:
            if subtask.id == subtask_id:
                self._subtasks.remove(subtask)


class Movetask:
    def get_where(self, task_id):
        task = self.get_task(task_id)
        where = task.status
        if where == "Normal":
            self.task_normal.remove_task(task)
        elif where == "Highlight":
            self.task_highlight.remove_task(task)
        elif where == "Finished":
            self.task_finished.remove_task(task)
        elif where == "Deleted":
            self.task_deleted.remove_task(task)
        return task

    def move_to_task_delete(self, task_id):
        task = self.get_where(task_id)
        task.status = "Deleted"
        self._task_deleted.task_list.append(task)

    def move_to_task_finish(self, task_id):
        task = self.get_where(task_id)
        task.status = "Finished"
        self._task_finished.task_list.append(task)

    def move_to_task_highlight(self, task_id):
        task = self.get_where(task_id)
        task.status = "Highlight"
        self._task_highlight.task_list.append(task)

    def move_to_task_normal(self, task_id):
        task = self.get_where(task_id)
        task.status = "Normal"
        self._task_normal.task_list.append(task)
