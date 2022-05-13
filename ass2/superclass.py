class All_command_front:
    def edit_tasklist_name(self, title, list_id):
        list_return = self.get_list(list_id)
        list_return.title = title

    def add_task(self, name, list_id):
        list_return = self.get_list(list_id)
        list_return.add_task(name)

    def edit_task(self, name, date, description, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.edit_task(name, date, description, task_id)

    def move_to_task(self, list_id, task_id, destination):
        list_return = self.get_list(list_id)
        list_return.move_to_task(task_id, destination)

    def add_subtask(self, name, list_id, task_id):
        list_return = self.get_list(list_id)
        list_return.add_subtask(name, task_id)

    def edit_subtask_detail(self, name, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.edit_subtask_detail_signal(name, task_id, subtask_id)

    def edit_subtask_status(self, list_id, task_id, subtask_id):
        list_return = self.get_list(list_id)
        list_return.edit_subtask_status_signal(task_id, subtask_id)

    # def remove_subtask(self, list_id, task_id, subtask_id):
    #     list_return = self.get_list(list_id)
    #     list_return.remove_subtask_signal(task_id, subtask_id)


class TaskAction:
    def edit_task(self, name, date, description, task_id):
        task = self.get_task(task_id)
        task.name = name
        task.due_date = date
        task.description = description


class SubtaskAction:
    def add_subtask(self, detail, task_id):
        task = self.get_task(task_id)
        task.add_subtask(detail)

    def edit_subtask_detail_signal(
        self,
        detail,
        task_id,
        subtask_id,
    ):
        task = self.get_task(task_id)
        task.edit_subtask_detail(detail, subtask_id)

    def edit_subtask_detail(self, detail, subtask_id):
        subtask = self.get_subtask(subtask_id)
        subtask.details = detail

    def edit_subtask_status_signal(self, task_id, subtask_id):
        task = self.get_task(task_id)
        task.edit_subtask_status(subtask_id)

    def edit_subtask_status(self, subtask_id):
        subtask = self.get_subtask(subtask_id)
        subtask.change_status()

    # def remove_subtask_signal(self, subtask_id, task_id):
    #     task = self.get_task(task_id)
    #     task.remove_subtask(subtask_id)

    # def remove_subtask(self, subtask_id):
    #     for subtask in self.subtasks:
    #         if subtask.id == subtask_id:
    #             self.subtasks.remove(subtask)


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

    def move_to_task(self, task_id, destination, dict):
        task = self.get_where(task_id)
        task.status = destination
        dict[destination].task_list.append(task)
