# You may need to install sympy once:
# pip install sympy

from sympy import randprime

def generate_large_primes(count, digits):
    """Generate 'count' different prime numbers, each with the given number of digits."""
    primes = set()
    lower = 10**(digits - 1)
    upper = 10**digits - 1

    while len(primes) < count:
        p = randprime(lower, upper)
        primes.add(p)

    return list(primes)

# Generate 10 different 100-digit primes
large_primes = generate_large_primes(10, 100)

# Print the results
for i, prime_num in enumerate(large_primes, start=1):
    print(f"Prime {i}:")
    print(prime_num)
    print(f"Digits: {len(str(prime_num))}")
    print("-" * 60)

#I used LLM but mostly understand the solution, after midterm's I try to solve without using LLM.
