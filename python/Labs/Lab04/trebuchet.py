# Author: Eugene Kozlakov
# Date: 9/24/2023
# Description: Has the user input various distances. Records the three largest distances and their indexes, and prints them out in descending order once the program is terminated.

dist1 = 0
dist2 = 0
dist3 = 0

trialIndex1 = 0
trialIndex2 = 0
trialIndex3 = 0

userInput = "Y" #Sentinel Value
trialCount = 1

while (userInput == "Y"):
  userDistance = int(input("--Please input an integer distance: "))

  if (userDistance > dist1):
    dist3 = dist2
    dist2 = dist1
    trialIndex3 = trialIndex2
    trialIndex2 = trialIndex1
    dist1 = userDistance
    trialIndex1 = trialCount
  elif (dist1 >= userDistance) and (userDistance > dist2):
    dist3 = dist2
    trialIndex3 = trialIndex2
    dist2 = userDistance
    trialIndex2 = trialCount
  elif (dist2 >= userDistance) and (userDistance > dist3):
    dist3 = userDistance
    trialIndex3 = trialCount

  userInput = input("Would you like to attempt another trial [Y/N]: ")
  trialCount += 1

print("these are the three largest distances, in descending order.")
print("Trial No. | Distance")
print(format(trialIndex1, '^-9d'), "|", format(dist1, "^-9"))
print(format(trialIndex2, '^-9d'), "|", format(dist2, "^-9"))
print(format(trialIndex3, '^-9d'), "|", format(dist3, "^-9"))