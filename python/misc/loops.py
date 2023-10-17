i = 0

while (i < 10):
  if(i%2 == 0):
    print("continuing")
    i += 1
    continue
  else:
    print(i)
    i+=1

userInput = 0
while(userInput != -1):
  userInput = int(input("Please input -1 to stop the loop and continue the program: "))

for x in range(0,20, 5):
  print (x)