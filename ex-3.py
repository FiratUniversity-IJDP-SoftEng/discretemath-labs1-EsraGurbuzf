def squareminusone(number3):
  primelist = allprime(100)
  for i in primelist:
    is_prime2 = True
    for j in range(2, i + 1):
      if i % j == 0:
        is_prime2 = False
    if is_prime2:
      primelist.append(i)
  return primelist

tell = int(input("Enter a number: "))
print(squareminusone(tell))
