# Question: Day 31: Create a decorator to measure function execution time.
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} executed in {end-start:.4f}s")
        return result
    return wrapper

@timer
def sample_function():
    time.sleep(1)

sample_function()
