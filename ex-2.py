def allprime(number2):
  primes = []
  for i in range(2, number2 + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
      if i % j == 0:
        is_prime = False
    if is_prime:
      primes.append(i)
  return primes

ask = int(input("Enter a number: "))
print(allprime(ask))
