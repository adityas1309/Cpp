# Question: Day 53: Create a context manager to measure execution time of code blocks.
from time import perf_counter
from contextlib import contextmanager

@contextmanager
def timer():
    start = perf_counter()
    yield
    end = perf_counter()
    print(f"Execution time: {end - start:.4f} seconds")

with timer():
    sum(range(1000000))
