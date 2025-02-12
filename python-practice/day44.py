# Question: Day 44: Implement threading to calculate squares and cubes simultaneously.
import threading

def square(n):
    print(f"Square: {n*n}")

def cube(n):
    print(f"Cube: {n*n*n}")

num = 5
t1 = threading.Thread(target=square, args=(num,))
t2 = threading.Thread(target=cube, args=(num,))

t1.start()
t2.start()
t1.join()
t2.join()
