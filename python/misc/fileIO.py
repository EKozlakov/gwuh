myFile = open("beebo.txt", 'r')
myOtherFile = open("obeeb.txt", 'w')

for lines in myFile:
  print(lines, end="")
  myOtherFile.write(lines[::-1])
myFile.close()


myOtherFile = open("obeeb.txt", 'r')
for lines in myOtherFile:
  print(lines, end="")

myOtherFile.close()
