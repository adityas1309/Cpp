# Question: Day 8: Write a Python program to check if a number is prime.
num = int(input("Enter a number: "))
# Prime check algorithm
is_prime = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is {'prime' if is_prime else 'not prime'}")
