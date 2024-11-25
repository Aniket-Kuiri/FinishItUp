# Main Class that defines all the methods for Finish It Up App
from task_store import TaskStore
from task_manager import TaskManager 
class FinishItUp():
    def __init__(self):
        self.task_store = TaskStore()
        task_list = self.task_store.get_all_tasks()
        current_task = self.task_store.get_current_task()
        completed_tasks = self.task_store.get_completed_tasks()
        self.task_manager = TaskManager(task_list, current_task, completed_tasks) 

    def add_task(self, name, type, description):
        tasks = self.task_manager.add_task(name, type, description)
        self.task_store.persist_tasks(tasks)
        return True

    def get_current_task(self):
        task, task_list, is_new = self.task_manager.get_current_task()
        if is_new:
            # print(task)
            # print(task_list)
            self.task_store.persist_tasks(task_list)
            self.task_store.persist_current_task(task)
        return task

    def complete_task(self, description, terminate):
        status, tasks, current_task, completed_tasks, err = self.task_manager.complete_task(description, terminate)
        if status:
            self.task_store.persist_tasks(tasks)
            self.task_store.persist_current_task(current_task)
            self.task_store.persist_completed_tasks(completed_tasks)
        return status, err

    def get_completed_task(self):
        completed_tasks_list =  self.task_manager.get_completed_tasks()
        return completed_tasks_list

    def reset(self):
        status, tasks, current_task, completed_tasks, err = self.task_manager.reset()
        if status:
            self.task_store.persist_tasks(tasks)
            self.task_store.persist_current_task(current_task)
            self.task_store.persist_completed_tasks(completed_tasks)        
        return status, err


