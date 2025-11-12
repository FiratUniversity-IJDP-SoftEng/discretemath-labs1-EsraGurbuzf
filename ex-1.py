def prime(number):
  if number < 2:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True
result = int(input("Enter a number: "))
print(prime(result))
