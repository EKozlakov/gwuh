list = ["Cat", "Dog", "Bird"]

for x in list:
  print(x)

print("\n")
for i in range(len(list)):
  print (i)

rows = 15
cols = 5
data = []
for row in range(rows):
  data += [[0]*cols]

for row in range(rows):
  print() #newline
  for col in range(cols):
    print(data[row][col], end="")