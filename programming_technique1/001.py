n = 12

if n % 3 == 0 and n % 5 == 0:
  o = "FizzBuzz"
elif n % 3 == 0:
  o = "Fizz"
elif n % 5 == 0:
  o = "Buzz"
else:
  o = ""

print(n,o)

import random as r
n = r.randint(1,127)

if n % 3 == 0 and n % 5 == 0:
  o = "FizzBuzz"
elif n % 3 == 0:
  o = "Fizz"
elif n % 5 == 0:
  o = "Buzz"
else:
  o = ""

print(n,o)

n = 12

if n % 3 == 0 and n % 5 == 0:
  print(n,"FizzBuzz")
elif n % 3 == 0:
  print(n,"Fizz")
elif n % 5 == 0:
  print(n,"Buzz")
else:
  print(n)

import random as r
n = r.randint(1,127)

if n % 3 == 0 and n % 5 == 0:
  print(n,"FizzBuzz")
elif n % 3 == 0:
  print(n,"Fizz")
elif n % 5 == 0:
  print(n,"Buzz")
else:
  print(n)