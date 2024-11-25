
from task import Task
import json
class TaskManager():
    def __init__(self, task_list, current_task, completed_task):
        self.task_list = task_list
        self.current_task = current_task
        self.completed_task = completed_task

    def add_task(self, name, type, description):
        # add to the task and return
        # updated task list
        task = Task(name, type, description)
        self.task_list.append(task.get_dict())
        return self.task_list

    def get_current_task(self):
        # return only the current task
        if self.current_task == []:
            self.current_task = self._select_task()
            # print(self.task_list)
            return self.current_task, self.task_list, True        
        return self.current_task, None, False

    def complete_task(self, description, terminate):
        # update current_task_list, completed task list
        # and current task list and return them

        # update the current task
        if self.current_task == []:
            return False, self.task_list, self.current_task, self.completed_task,  "No task to complete"
        
        task_json = self.current_task[0]
        task = Task()
        task.add_json(task_json)
        task.set_timestamp()
        type = task.get_type()

        # move it to completed task if not repeatable or if repeatable and terminate

        # move it to current tasks if repeatable with new description and weightage

        task_json = task.get_json()
        self.completed_task.append(task_json)
        if type == 'repetitive' and not terminate:
            task.reset()
            task.set_description(description)
            self.current_task.append(task.get_json())

        # select a new current task
        self.task_list = self._select_task()

        # return all the values
        return True, self.task_list, self.current_task, self.completed_task, ""

    def get_completed_tasks(self):
        # return only the completed tasks
        pass

    def reset(self):
        # reset current_task_list, completed task list
        # and current task and return them 
        pass

    def _select_task(self):
        if self.task_list == []:
            return []
        self.task_list = sorted(self.task_list, key=lambda x: x['weightage'])
        selected_task = self.task_list.pop()
        return [selected_task]

    def _update_task_weightage(self):
        pass