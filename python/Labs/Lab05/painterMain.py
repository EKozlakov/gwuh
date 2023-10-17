# Author: Eugene Kozlakov
# Date: 9/29/2023
# Description: Outputs ASCII art depending on user's input.
# I did some research to do this the best way I know how. Below are my sources which I'd like to credit:
# -Longest string in a list: https://www.geeksforgeeks.org/python-longest-string-in-list/
# -Removing trailing newline: https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
# -Basic Python File IO: https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/
#
# +This is the main body of the the program. It uses functions from 'painterFuncs.py'
import painterFuncs

def main():
  artSelection, borderSelection = painterFuncs.intro()

  if(artSelection == 1):
    painterFuncs.sleepingCat(borderSelection)
  elif(artSelection == 2):
    painterFuncs.sailingShip(borderSelection)
  elif(artSelection == 3):
    painterFuncs.window(borderSelection)
  elif(artSelection == 4):
    painterFuncs.warning(borderSelection)
  else:
    print("Apologies, we don't seem to have that. Goodbye.")
    exit(-1)

main()