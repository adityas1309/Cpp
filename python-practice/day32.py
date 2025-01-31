# Question: Day 32: Generate first N prime numbers using generator functions.
def prime_generator(n):
    num = 2
    count = 0
    while count < n:
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            yield num
            count += 1
        num += 1

# Print first 10 primes
print(list(prime_generator(10)))
