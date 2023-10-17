"""
Author: Eugene Kozlakov
Date: 9/29/2023
Description: Functions for painterMain.py file. Split from the original painter.py file.
"""

def printHeaderFooter(borderSelection, size):
  """
  Prints a image size-dependent line of the character inputted in 'borderSelection' in order to properly fit a "frame" to the ASCII
  
  :param borderSelection: Contains a string character input by the user. This will be used to make the string.

  :type borderSelection: string

  :param size: Pre-calculated size of the "frame header" or "footer" -- will indicate how many times character needs to be printed to form the top and bottom bounds.

  :type size: integer

  :return: NONE

  Note: +4 is added to size param to account for 2 whitespaces after image and and 2 columns of "frame" character on both ends of each line.
  
  """
  for i in range(size+4): #why +4? I honestly couldnt tell you. i plugged it in and it seemed to just work. something with the whitespaces.
    print(borderSelection, end="")
  print() #newline print


def sleepingCat(borderSelection):
  """
  Prints an image of a sleeping cat. Prints both sides of image "frame".
  
  :param borderSelection: User-defined "frame" character
  :type borderSelection: string
  
  :param [variant]IMG: Name varies depending on what is being printed. A list containing each line of the ASCII art as an individual item.
  :type [variant]IMG: list
  
  :param f: file object, with which the lines for the ASCII art are taken in.
  :type f: typing.IO (IO[str]) (?; not sure about this one)

  :param row: Counter for rows. only used in for loop.
  :type row: integer

  :param rowSize: The "longest" (widest) string in the list. This is used to reserve characters for printing the ASCII art and determining Frame header and footer size.
  :type rowSize: integer
  
  :return: NONE

  Algorithm:
  1. Saves each line of the .txt file as an item in the list '[variant]IMG'
  2. Finds "longest line" (widest part of ASCII image) and saves it. This data is sent to "printHeaderFooter" to print the header and footer.
  3. Prints each line, appending the user-selected frame character at the beginning and end of each line, reserving the # of characters found for 'rowSize'
  4. Prints "footer" via printHeaderFooter function.
  5. Done. 
  """
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
  """
  Prints an image of a sleeping cat. Prints both sides of image "frame".
  
  :param borderSelection: User-defined "frame" character
  :type borderSelection: string
  
  :param [variant]IMG: Name varies depending on what is being printed. A list containing each line of the ASCII art as an individual item.
  :type [variant]IMG: list
  
  :param f: file object, with which the lines for the ASCII art are taken in.
  :type f: typing.IO (IO[str]) (?; not sure about this one)

  :param row: Counter for rows. only used in for loop.
  :type row: integer

  :param rowSize: The "longest" (widest) string in the list. This is used to reserve characters for printing the ASCII art and determining Frame header and footer size.
  :type rowSize: integer
  
  :return: NONE

  Algorithm:
  1. Saves each line of the .txt file as an item in the list '[variant]IMG'
  2. Finds "longest line" (widest part of ASCII image) and saves it. This data is sent to "printHeaderFooter" to print the header and footer.
  3. Prints each line, appending the user-selected frame character at the beginning and end of each line, reserving the # of characters found for 'rowSize'
  4. Prints "footer" via printHeaderFooter function.
  5. Done. 
  """
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
  """
  Prints an image of a sleeping cat. Prints both sides of image "frame".
  
  :param borderSelection: User-defined "frame" character
  :type borderSelection: string
  
  :param [variant]IMG: Name varies depending on what is being printed. A list containing each line of the ASCII art as an individual item.
  :type [variant]IMG: list
  
  :param f: file object, with which the lines for the ASCII art are taken in.
  :type f: typing.IO (IO[str]) (?; not sure about this one)

  :param row: Counter for rows. only used in for loop.
  :type row: integer

  :param rowSize: The "longest" (widest) string in the list. This is used to reserve characters for printing the ASCII art and determining Frame header and footer size.
  :type rowSize: integer
  
  :return: NONE

  Algorithm:
  1. Saves each line of the .txt file as an item in the list '[variant]IMG'
  2. Finds "longest line" (widest part of ASCII image) and saves it. This data is sent to "printHeaderFooter" to print the header and footer.
  3. Prints each line, appending the user-selected frame character at the beginning and end of each line, reserving the # of characters found for 'rowSize'
  4. Prints "footer" via printHeaderFooter function.
  5. Done. 
  """
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
  """
  Prints an image of a sleeping cat. Prints both sides of image "frame".
  
  :param borderSelection: User-defined "frame" character
  :type borderSelection: string
  
  :param [variant]IMG: Name varies depending on what is being printed. A list containing each line of the ASCII art as an individual item.
  :type [variant]IMG: list
  
  :param f: file object, with which the lines for the ASCII art are taken in.
  :type f: typing.IO (IO[str]) (?; not sure about this one)

  :param row: Counter for rows. only used in for loop.
  :type row: integer

  :param rowSize: The "longest" (widest) string in the list. This is used to reserve characters for printing the ASCII art and determining Frame header and footer size.
  :type rowSize: integer
  
  :return: NONE

  Algorithm:
  1. Saves each line of the .txt file as an item in the list '[variant]IMG'
  2. Finds "longest line" (widest part of ASCII image) and saves it. This data is sent to "printHeaderFooter" to print the header and footer.
  3. Prints each line, appending the user-selected frame character at the beginning and end of each line, reserving the # of characters found for 'rowSize'
  4. Prints "footer" via printHeaderFooter function.
  5. Done. 
  """
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
  """
  Welcomes user and provides them with options.

  :param artSelection: User inputs a digit to select what art they would like to see.
  :type artSelection: integer

  :param borderSelection: User defined "frame" character used to make sides, header, and footer.
  """
  print("Welcome to painter.py!\nWhat painting would you like to see?")
  print("   [1] Cat nap.")
  print("   [2] USS Satisfaction.")
  print("   [3] A Window.")
  print("   [4] No Smoking!")
  artSelection = int(input("Please input a number indicating what you would like to do: "))
  borderSelection = input("Please input the character indicating what kind of border you would like on your image: ")
  return artSelection, borderSelection