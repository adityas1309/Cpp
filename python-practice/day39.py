# Question: Day 39: Use multiprocessing to calculate square of numbers in parallel.
import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)
    print(results)  # [1, 4, 9, 16, 25]
