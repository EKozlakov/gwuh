# Author: Eugene Kozlakov
# Date: 9/29/2023
# Description: Outputs ASCII art depending on user's input. An improved version.
# I did some research to do this the best way I know how. Below are my sources which I'd like to credit:
# -Longest string in a list: https://www.geeksforgeeks.org/python-longest-string-in-list/
# -Removing trailing newline: https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
# -Basic Python File IO: https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/
# -centering strings: https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/center/python-string-center/
# -Italics on console: https://stackoverflow.com/questions/13559276/can-i-write-italics-to-the-python-shell


def printHeaderFooter(borderSelection, size):
  for i in range(size+4): #why +4? I honestly couldnt tell you. i plugged it in and it seemed to just work. something with the whitespaces.
    print(borderSelection, end="")
  print() #newline print


def paint(borderSelection, fileName, comment):
  img = []
  with open(fileName+'.txt') as f:
    img = f.readlines()

  rowSize = len(max(img, key = len)) #finds longest row in list, sets that to rowsize.

  printHeaderFooter(borderSelection, rowSize)
  #breakpoint()
  for row in range(len(img)):
    print(borderSelection, format(img[row].rstrip(), str(rowSize)), borderSelection)
  printHeaderFooter(borderSelection, rowSize)
  print(comment.center(rowSize+4), "\x1B[0m")

def intro():
  print("Welcome to painter.py!\nWhat painting would you like to see?")
  print("   [1] Cat nap.")
  print("   [2] USS Satisfaction.")
  print("   [3] A Window.")
  print("   [4] No Smoking!")
  print("   [5] (Your painting here)")
  artSelection = int(input("Please input a number indicating what you would like to do: "))
  borderSelection = input("Please input the character indicating what kind of border you would like on your image: ")
  return artSelection, borderSelection
 


def main():
  artSelection, borderSelection = intro()
  comment = ""
  if(artSelection == 1):
    comment = "\x1B[3mThe cat is sound asleep."
    paint(borderSelection, 'sleepingCat', comment)
  elif(artSelection == 2):
    comment = "\x1B[3mUSS Satisfaction. Wish I was there."
    paint(borderSelection, 'sailingShip', comment)
  elif(artSelection == 3):
    comment = "\x1B[3mA window and a flowerpot."
    paint(borderSelection, 'window', comment)
  elif(artSelection == 4):
    comment = "\x1B[3mBetter take note."
    paint(borderSelection, 'warning', comment)
  elif(artSelection == 5):
    comment = "\x1B[3m"
    userFilename = input("Please input the name of your file, without the .txt ending: ")
    comment += input("Please input the comment you would like your painting to have: ")
    paint(borderSelection, 'warning', comment)
  else:
    print("Apologies, we don't seem to have that. Please try again later.")
    exit(-1)

main()
print("\nI hope you enjoyed the painting. Take care.")
