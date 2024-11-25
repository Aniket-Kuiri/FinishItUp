
from task import Task
import random
class TaskManager():
    def __init__(self, task_list, current_task, completed_task):
        self.task_list = task_list
        self.current_task = current_task
        self.completed_task = completed_task

    def add_task(self, name, type, description):
        task = Task(name, type, description)
        self.task_list.append(task.get_dict())
        return self.task_list

    def get_current_task(self):
        if self.current_task == []:
            self.current_task = self._select_task()
            return self.current_task, self.task_list, True        
        return self.current_task, None, False

    def complete_task(self, description, terminate):
        # update the current task
        if self.current_task == []:
            return False, self.task_list, self.current_task, self.completed_task,  "No task to complete"        
        task_dict = self.current_task[0]
        task = Task()
        task.add_dict(task_dict)
        task.set_timestamp()
        type = task.get_type()
        # move it to completed task if not repeatable or if repeatable and terminate
        # move it to current tasks if repeatable with new description and weightage
        task_dict = task.get_dict()
        self.completed_task.append(task_dict)
        task_to_add = None
        if type == 'repetitive' and not terminate:
            task.reset()
            task.set_description(description)
            task_to_add = task.get_dict()
        # select a new current task
        self.current_task = self._select_task()
        # update weightage of all other pending tasks
        self.task_list = self._update_task_weightage()
        # return all the values
        if task_to_add:
            self.task_list.append(task_to_add)
        return True, self.task_list, self.current_task, self.completed_task, ""

    def get_completed_tasks(self):
        return self.completed_task

    def reset(self):
        self.current_task = []
        self.task_list = []
        self.completed_task = [] 
        return True, self.task_list, self.current_task, self.completed_task, ""

    def _select_task(self):
        if self.task_list == []:
            return []
        self.task_list = sorted(self.task_list, key=lambda x: -x['weightage'])
        max_weightage = None
        max_weightage_count = 0
        for task in self.task_list:
            if max_weightage == None:
                max_weightage = task['weightage']
            elif task['weightage'] == max_weightage:
                max_weightage_count += 1
            else:
                break        
        selected_task = self.task_list.pop(random.randint(0, max_weightage_count))
        return [selected_task]

    def _update_task_weightage(self):
        updated_task_list = []
        for task in self.task_list:
            task_inst = Task()
            task_inst.add_dict(task)
            task_inst.update_weightage()
            updated_task_list.append(task_inst.get_dict())
        return updated_task_list