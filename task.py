# Class to deifne structure of a task
import uuid
from datetime import datetime
class Task():
    def __init__(self, name=None, type=None, description=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = type
        self.description = description
        self.weightage = 0
        self.timestamp = None

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_type(self):
        return self.type

    def set_type(self, task_type):
        self.type = task_type

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def get_weightage(self):
        return self.weightage
    
    def update_weightage(self):
        # update based on type 
        if self.type == 'one-time':
            self.weightage += 1
        else:
            self.weightage += 2

    def set_weightage(self, weightage):
        # update based on type 
        self.weightage = weightage
    
    def get_timestamp(self):
        return self.timestamp
    
    def set_timestamp(self):
        # set current timestamp
        self.timestamp = str(datetime.now())

    def update_timestamp(self):
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
        task_json['timestamp'] = self.timestamp
        return task_json
    
    def add_dict(self, dict):
        self.set_id(dict['id'])
        self.set_name(dict['name'])
        self.set_type(dict['type'])
        self.set_description(dict['description'])
        self.set_weightage(dict['weightage'])

    def reset(self):
        self.set_weightage(0)
        self.update_timestamp()