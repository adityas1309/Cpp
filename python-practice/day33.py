# Question: Day 33: Create a context manager for file operations that handles exceptions.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return True

with FileManager('test.txt', 'w') as f:
    f.write('Hello Context Manager!')
