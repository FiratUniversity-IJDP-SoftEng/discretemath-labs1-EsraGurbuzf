def prime(number):
  if number < 2:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

all_primes = True
for v in range(0, 40):
  value = v**2 + v + 41
  if not prime(value):
    print(f"v = {v}, value = {value} → NOT prime")
    all_primes = False
  else:
    print(f"v = {v}, value = {value} → prime")

k = 40
value = k**2 + k + 41
print(f"\nWhen k = 40 → {value} → prime? {prime(value)}")
