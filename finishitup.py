# Main Class that defines all the methods for Finish It Up App
from task_store import TaskStore
from task_manager import TaskManager 
class FinishItUp():
    def __init__(self):
        self.task_store = TaskStore()
        task_list = self.task_store.get_all_tasks()
        # get current task
        # get completed tasks
        self.task_manager = TaskManager(task_list) 

    def add_task(self, name, type, description):
        # add and persist
        return True

    def get_current_task(self):
        return None

    def complete_task(self, task_id, description, terminate):
        return True, ""

    def get_completed_task(self):
        return []

    def reset(self):
        return True


