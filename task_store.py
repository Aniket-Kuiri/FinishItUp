# Persistence class for Finish It Up App
import os
import json
from pathlib import Path

class TaskStore():
    def __init__(self):
        self.dir_name = "data"
        self.task_file = "task_file.json"
        self.current_task_file = "current_task.json"
        self.completed_task_file = "completed_task.json"
        self._create_dir()
        self._create_file(self.task_file)
        self._create_file(self.current_task_file)
        self._create_file(self.completed_task_file)

    def _create_dir(self):
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

    def _create_file(self, name):
        full_path = os.path.join(self.dir_name, name)
        if not os.path.exists(full_path):
            Path(full_path).touch()
            with open(full_path, 'w') as file:
                json.dump([], file)

    def _delete_file(self, name):
        full_path = os.path.join(self.dir_name, name)
        if os.path.exists(full_path):
            os.remove(full_path)

    def _write_file(self, name, content):
        try:
            full_path = os.path.join(self.dir_name, name)
            if os.path.exists(full_path):
                with open(full_path, 'w') as file:
                    json.dump(content, file)
                    return True
        except Exception as e:
            return False
        return False

    def _read_file(self, name):
        full_path = os.path.join(self.dir_name, name)
        if os.path.exists(full_path):
            with open(full_path, 'r') as file:
                data = json.load(file)
                return data
        return None

    def get_all_tasks(self):
        task_list = self._read_file(self.task_file)
        return task_list

    def get_completed_tasks(self):
        completed_tasks_list = self._read_file(self.completed_task_file)
        return completed_tasks_list

    def get_current_task(self):
        current_task = self._read_file(self.current_task_file)
        return current_task

    def persist_tasks(self, tasks):
        status = self._write_file(self.task_file, tasks)
        return status

    def persist_current_task(self, task):
        status = self._write_file(self.current_task_file, task)
        return status       

    def persist_completed_tasks(self, tasks):
        status = self._write_file(self.completed_task_file, tasks)
        return status
    
    def reset(self):
        self._delete_file(self.task_file)
        self._delete_file(self.current_task_file)
        self._delete_file(self.completed_task_file)
