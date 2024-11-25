# Class to deifne structure of a task
import uuid
import json
class Task():
    def __init__(self, name=None, type=None, description=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = type
        self.description = description
        self.weightage = 0
        self.timestamp = None

    def update_weightage(self):
        # update based on type 
        pass

    def get_weightage(self):
        return self.weightage
    
    def set_description(self, description):
        self.description = description

    def set_timestamp(self):
        # set current timestamp
        self.timestamp = None

    def get_dict(self):
        # return in JSON format,
        # if it is a completed task 
        # it would also return a JSON
        task_json = {}
        task_json['id'] = self.id
        task_json['name'] = self.name
        task_json['type'] = self.type
        task_json['description'] = self.description
        task_json['weightage'] = self.weightage
        return task_json