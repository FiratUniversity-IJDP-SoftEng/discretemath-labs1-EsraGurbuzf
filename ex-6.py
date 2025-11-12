
# Find composite n <= 10000 with 2^n ≡ 2 (mod n)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n**0.5)
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

pseudoprimes = []
for n in range(2, 10001):
    if not is_prime(n):
        if pow(2, n, n) == 2 % n:   # fast modular exponentiation
            pseudoprimes.append(n)

print("Count:", len(pseudoprimes))
print(pseudoprimes)

#I used LLM but mostly understand the solution, after midterm's I try to solve without using LLM.
