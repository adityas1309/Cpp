# Question: Day 50: Create a recursive directory size calculator.
import os

def dir_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += dir_size(entry.path)
    return total

print(f"Directory size: {dir_size('.')} bytes")
