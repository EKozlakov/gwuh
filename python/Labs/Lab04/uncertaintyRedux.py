# Author: Eugene Kozlakov
# Date: 9/23/2023
# Description: Plays a position guessing game with the user. The
# user has to guess a point within a 10x10 grid.
#   +updated to give the user multiple chances

partXPos = 4
partYPos = 6

guessCount = 3 ##number of guesses user has

while(guessCount > 0):

  print("\nYou have %d guesse(s) left" % (guessCount))

  userXPos = int(input("The particle is somewhere in this space! What do you think its x coordinate is (1-10)? ")) #Prompt the user for a number between 1 and 10, inclusively

  userYPos = int(input("What do you think its y coordinate is (1-10)? ")) #Prompt the user for a number between 1 and 10, inclusively

  if userXPos == partXPos and userYPos == partYPos: 
      print("Good guess! (%d,%d) was the position!" % (partXPos,partYPos)) #If the position is the same, tell the user they found the particle
      break
  if userXPos == partXPos:
    print("No good! You got the X-ccordinate right though! X = (%d)" % (userXPos)) 
  elif userXPos > partXPos:
    print("No good! The particle's X-coordinate is LESS THAN your guess, X = (%d)" % (userXPos))
  elif userXPos < partXPos:
    print("No good! The particle's X-coordinate is GREATER THAN your guess, X = (%d)" % (userXPos))
  
  if userYPos == partYPos:
    print("No good! You got the Y-coordinate right though! Y = (%d)" % (userYPos))
  elif userYPos > partYPos:
    print("No good! The particle's Y-coordinate is LESS THAN your guess, Y = (%d)" % (userYPos))
  elif userYPos < partYPos:
    print("No good! The particle's Y-coordinate is GREATER THAN your guess, Y = (%d)" % (userYPos))
      
  guessCount -= 1
else:
  print("You ran out of guesses! (%d,%d) was the position!" % (partXPos,partYPos))  #Otherwise, tell the user they did not find it