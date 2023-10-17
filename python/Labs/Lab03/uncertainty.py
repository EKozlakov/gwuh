import pdb


particleX = 3
particleY = 5



#pdb.set_trace()

while(True):
  guessX = int(input("Please input a guess for Particle X coordinate between 1 and 10: "))
  guessY = int(input("Please input a guess for Particle Y coordinate between 1 and 10: "))
  if((guessX == particleX) and (guessY == particleY)):
    print("Congrats! You guess the particle's position correctly! You win! ...something.")
    break
  elif((guessX > 10) or (guessX < 1) or (guessY > 10) or (guessY < 1)): #using range: if(guessX not in range(1,11)). do not use !=.
    print("One of your guesses was outside of the parameters. You lose. Try again. \n")
  else:
    print("You guessed incorrectly. You lose. Try again. \n")

quit()