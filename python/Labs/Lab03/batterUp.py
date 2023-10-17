import random

distance = random.randint(0,451)

if(distance > 400):
  print(f"The batter hit a home run, hitting the ball to a distance of {distance} feet! The team gets a run.")
elif(135 <= distance <= 400):
  print(f"The ball goes into the outfield at {distance} feet, and the batter is SAFE in third base.")
elif(10 <= distance <= 134):
  print(f"The ball makes it into the infield at {distance} feet, and the batter is SAFE at second base.")
elif(1 <= distance <= 9):
  print(f"The batter bunted the ball, hitting it a distance of {distance} feet. The batter is SAFE at first base.")
elif(distance == 0):
  print("Strike!")

quit()