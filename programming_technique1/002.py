#課題①
y = []
i = 1
while i <=16:
  y.append(2**i)
  i += 1
print(y)

#課題①
y = []
for i in range(1,17):
  y.append(2**i)
  i += 1
print(y)

#課題②
import random
char = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
"n","o","p","q","r","s","t","u","v","w","x","y","z",
"0","1","2","3","4","5","6","7","8","9"]
i = 0
p = []
while i <= 4:
  p.append(char[random.randint(0,35)])
  i += 1
print(p[0]+p[1]+p[2]+p[3]+p[4])

#課題②
import random
char = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
"n","o","p","q","r","s","t","u","v","w","x","y","z",
"0","1","2","3","4","5","6","7","8","9"]
p = []
for i in range(0,5):
  p.append(char[random.randint(0,35)])
  i += 1
print(p[0]+p[1]+p[2]+p[3]+p[4])