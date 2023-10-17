# Author: Eugene Kozlakov
# Date: 9/29/2023
# Description: Outputs ASCII art depending on user's input.
# I did some research to do this the best way I know how. Below are my sources which I'd like to credit:
# -Longest string in a list: https://www.geeksforgeeks.org/python-longest-string-in-list/
# -Removing trailing newline: https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
# -Basic Python File IO: https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/




def printHeaderFooter(borderSelection, size):
  for i in range(size+4): #why +4? I honestly couldnt tell you. i plugged it in and it seemed to just work. something with the whitespaces.
    print(borderSelection, end="")
  print() #newline print


def sleepingCat(borderSelection):
  catIMG = []
  with open('sleepingCat.txt') as f:
    catIMG = f.readlines()

  rowSize = len(max(catIMG, key = len)) #finds longest row in list, sets that to rowsize.

  printHeaderFooter(borderSelection, rowSize)
  #breakpoint()
  for row in range(len(catIMG)):
    print(borderSelection, format(catIMG[row].rstrip(), str(rowSize)), borderSelection)
  printHeaderFooter(borderSelection, rowSize)

def sailingShip(borderSelection):
  shipIMG = []
  with open('sailingShip.txt') as f:
    shipIMG = f.readlines() #read in every single line of .txt as an element in the list 

  rowSize = len(max(shipIMG, key = len)) #finds longest row in list, sets that to rowsize.

  printHeaderFooter(borderSelection, rowSize)
  #breakpoint()
  for row in range(len(shipIMG)):
    print(borderSelection, format(shipIMG[row].rstrip(), str(rowSize)), borderSelection)
  printHeaderFooter(borderSelection, rowSize)

def window(borderSelection):
  winIMG = []
  with open('window.txt') as f:
    winIMG = f.readlines() #read in every single line of .txt as an element in the list 

  rowSize = len(max(winIMG, key = len)) #finds longest row in list, sets that to rowsize.

  printHeaderFooter(borderSelection, rowSize)
  #breakpoint()
  for row in range(len(winIMG)):
    print(borderSelection, format(winIMG[row].rstrip(), str(rowSize)), borderSelection)
  printHeaderFooter(borderSelection, rowSize)

def warning(borderSelection):
  warnIMG = []
  with open('warning.txt') as f:
    warnIMG = f.readlines() #read in every single line of .txt as an element in the list 

  rowSize = len(max(warnIMG, key = len)) #finds longest row in list, sets that to rowsize.

  printHeaderFooter(borderSelection, rowSize)
  #breakpoint()
  for row in range(len(warnIMG)):
    print(borderSelection, format(warnIMG[row].rstrip(), str(rowSize)), borderSelection)
  printHeaderFooter(borderSelection, rowSize)



def intro():
  print("Welcome to painter.py!\nWhat painting would you like to see?")
  print("   [1] Cat nap.")
  print("   [2] USS Satisfaction.")
  print("   [3] A Window.")
  print("   [4] No Smoking!")
  artSelection = int(input("Please input a number indicating what you would like to do: "))
  borderSelection = input("Please input the character indicating what kind of border you would like on your image: ")
  return artSelection, borderSelection
 


def main():
  artSelection, borderSelection = intro()

  if(artSelection == 1):
    sleepingCat(borderSelection)
  elif(artSelection == 2):
    sailingShip(borderSelection)
  elif(artSelection == 3):
    window(borderSelection)
  elif(artSelection == 4):
    warning(borderSelection)
  else:
    print("Apologies, we don't seem to have that. Goodbye.")
    exit(-1)

main()
