#問題
#以下のリスト dataがある。(50個の1~100までの乱数) 
#重複している数値を求めてください。
#data = [87, 70, 82, 37, 29, 39, 57, 41, 52, 63, 31, 49, 87, 90, 99, 12, 23, 
#       65, 52, 77, 69, 8, 22, 78, 5, 75, 2, 85, 14, 55, 96, 82, 53, 32, 60, 5, 13, 5, 
#       27, 32, 55, 90, 98, 16, 16, 38, 49, 10, 30, 77]



data = [87, 70, 82, 37, 29, 39, 57, 41, 52, 63, 31, 49, 87, 90, 99, 12, 23, 
65, 52, 77, 69, 8, 22, 78, 5, 75, 2, 85, 14, 55, 96, 82, 53, 32, 60, 5, 13, 5, 
27, 32, 55, 90, 98, 16, 16, 38, 49, 10, 30, 77]

duplication = list()  #重複している数値を入れるリスト

for first in range(len(data)):
  for second in range(len(data)):
    if first != second:
      if data[first] == data[second]:
        if data[first] not in duplication:
          duplication.append(data[first])

print(duplication)
