# Question: Day 52: Implement a generator function to produce Fibonacci numbers.
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_gen()
print([next(fib) for _ in range(10)])
