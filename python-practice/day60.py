# Question: Day 60: Final Project: Create a CLI task manager with file storage.
import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self._load_tasks()
    
    def _load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                return json.load(f)
        return []
    
    def _save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)
    
    def add_task(self, description):
        self.tasks.append({'description': description, 'completed': False})
        self._save_tasks()
    
    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else " "
            print(f"{i}. [{status}] {task['description']}")
    
    def complete_task(self, index):
        if 0 <= index-1 < len(self.tasks):
            self.tasks[index-1]['completed'] = True
            self._save_tasks()

# Example usage:
manager = TaskManager()
manager.add_task("Learn Python")
manager.add_task("Build projects")
manager.complete_task(1)
manager.list_tasks()
