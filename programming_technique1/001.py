#FizzBuzz問題
#数値n が3で割り切れる場合は、 Fizz と出力。
#数値n が5で割り切れる場合は、 Buzz と出力。
#数値n が3と5どちらでも割り切れる場合は、 FizzBuzz と出力。
#n も一緒に出力せよ。 上記に該当しない数値の場合はnのみ出力する。

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
