x = 0

for i in range(0,10):
  x += 1
  for j in range(0,10):
    if i == 3:
      print("breaking out of internal loop")
      break
  print(x)