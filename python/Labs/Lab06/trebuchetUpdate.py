import pdb

# Author: Eugene Kozlakov
# Date: 10/8/2023
# Description: This program allows the user to enter in a number of distances
# that their trebuchet's projectile was thrown and then displays the top three
# distances to the user
# + Updated to use lists

#Variables storing the distance
distances = [0, 0, 0] #first in list will be highest

#Variables storing the tirlas with the farthest distances
trial = [0, 0, 0] #first in list will be highest

#Help determines if the user wishes to add in additional high distances
keepGoing = "Y"

trialCount = 1

#So long as keepGoing is Y, keep adding in more trials
while keepGoing == "Y":
    distance = int(input(f"Please enter your distance for trial {trialCount}: "))

    #If the new distance is farther than the farthest distance, replace it
    #and shift everything else down
    if distance > distances[0]:
        distances[2] = distances[1]
        distances[1] = distances[0]
        distances[0] = distance        
        trial[2] = trial[1]
        trial[1] = trial[0]
        trial[0] = trialCount
    #If the new distance is distance than the second distance distance, replace it
    #and shift everything else down    
    elif distance > distances[1]:
        #breakpoint()
        distances[2] = distances[1]
        distances[1] = distance
        trial[2] = trial[1]
        trial[1] = trialCount
    #If the new distance is distance than the third distance distance, replace it    
    elif distance > distances[2]:
        distances[2] = distance
        trial[2] = trialCount

    keepGoing = input("Would you like to input another trial? (Y/N): ")
    
    trialCount += 1

#Output the highest distances and the initials of those people
print()
print("The top three distances for the trebuchet are:", )
print("(1) Trial No.", trial[0],"|", distances[0], "ft.")
print("(2) Trial No.", trial[1],"|", distances[1], "ft.")
print("(3) Trial No.", trial[2],"|", distances[2], "ft.")
