# Question: Day 23: Generate prime numbers up to N using Sieve of Eratosthenes algorithm.
def sieve(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for current in range(2, int(n**0.5)+1):
        if sieve[current]:
            for multiple in range(current*current, n+1, current):
                sieve[multiple] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

print(sieve(50))  # Primes up to 50
