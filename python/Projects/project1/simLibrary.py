import matplotlib.pyplot as plt
import os
import pdb
from time import sleep
from copy import deepcopy #imported because it turns out python list.copy function only makes a shallow copy that maintains all ref pointers. this screwed with my functionality.
# Author: Eugene Kozlakov
# Date: 10/15/2023
# Description: Library for SimEngine.py to execute a simualation of disease spread.

def count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day): #runs a count of all peoples, with day being index. presumes indexing is reliable.
  infectiousCount.append(0)
  susceptibleCount.append(0)
  recoveredCount.append(0)
  #breakpoint()
  for rows in range(len(regionMap)):
    for cols in range(len(regionMap[rows])):
      match regionMap[rows][cols]:
        case "i":
          infectiousCount[day] += 1
        case "s":
          susceptibleCount[day] += 1
        case "r":
          recoveredCount[day] += 1
  #breakpoint()
  return infectiousCount, susceptibleCount, recoveredCount


def printMap(map): #prints map.
  """
  Note: When colors are painted in the terminal, and the terminal window is resized, you get some of the row colors "running" off
  to the edge of the screen. This is supposedly an old issue that has only recently been fixed in Windows Terminal (please see: 
  https://github.com/microsoft/terminal/pull/12637), but as far as I can tell this has not reached other terminals yet -- at least,
  it hasn't reached mine. Just be wary of these issues as it can make the coloring of the cells look VERY ugly.
  """
  endSeq = " \x1B[0;0;0m" #ends ANSII escape sequence. Space added on purpose -- for formatting.
  redSeq = "\x1b[1;31;41m" #redBlock ANSII escape sequence
  yelSeq = "\x1b[1;33;43m" #yellow ANSII escape sequence
  greSeq = "\x1b[1;32;42m" #green ANSII escape sequence
  bluSeq = "\x1b[1;36;46m" #blue ANSII escape sequnece

  for rows in range(len(map)):   
    for cols in range(len(map[rows])):
      match map[rows][cols]:
        case "i":
          print(redSeq, "i", end=endSeq)
        case "s":
          print(yelSeq, "s", end= endSeq)
        case "r":
          print(greSeq, "r", end= endSeq)
        case "v":
          print(bluSeq, "v", end=endSeq)
        case _: #undefined case. source: https://stackoverflow.com/questions/68804209/how-to-do-an-else-default-in-match-case
          print(map[rows][cols], end=" ")
    print(endSeq) #newline
  print(endSeq) #newline. end sequence printed to eliminaet runoff.


def findInfected(infectionDate, day): #find all that are infected on current day. this will help in finding all adjacent cells to be infected "tomorrow"
  locations = []
  for i in range(len(infectionDate)):
    for j in range(len(infectionDate[i])):
        if(infectionDate[i][j] == day):
          locations.append([i,j])
  return locations


def findRecovered(regionMap, day, infectiousPeriod, infectionDate): #checks day of infection, infectionMap, and checks cells for passed threshold time.
  for i in range(len(infectionDate)):
    for j in range(len(infectionDate[i])):
        if(infectiousPeriod <= ((day+1) - infectionDate[i][j])): #because we are doing these updates "overnight", we have to account for what will happen "tomorrow." Therefore, we need to act as if we tallying day of, before printing -- like at "midnight updates."
          regionMap[i][j] = 'r'
  return regionMap

def plotEpidemic(infectiousCount, susceptibleCount, recoveredCount, day):
  time = list(range(day + 1)) #+1 to account for exclusivity of range functions

  plt.plot(time, susceptibleCount, marker='o', label = 'Susceptible', color = "orange" )
  plt.plot(time, infectiousCount, marker ='x', label = 'Infected', color = "red")
  plt.plot(time, recoveredCount, marker='^', label = 'Recovered', color = "green")
  plt.grid(which = "both", axis = "both")
  plt.legend(loc = "best")

  plt.title("Graph of Epidemic Group States over Outbreak Period")
  plt.xlabel("Day")
  plt.ylabel("Number of people")
  plt.show()

def scanForThreshold(regionMap, row, col, threshold, mapLength, mapWidth, infectionDate, day):
  iCounter = 0

  for i in range(row-1, row+2): #+2 rather than +1 to account for exclusivity of last term of range function
      if((i < 0) or (mapLength <= i)):  #if we're scanning a cell that is out of bounds, just skip it and go on.
        continue        
      for j in range(col-1, col+2):
        if((j < 0) or (mapWidth <= j)):
          continue 
        if((regionMap[i][j] == 'i') and (infectionDate[i][j] <= day)):
          #breakpoint()
          iCounter+=1

  if(threshold <= iCounter):
    return True
  else:
    return False

def updateMap(regionMap, threshold, day, infectionDate, mapLength, mapWidth, infectiousPeriod):
  currentInfected = []
  currentInfected  = findInfected(infectionDate, day) #successfully passes back coordinates.

  #breakpoint()
  for pair in currentInfected: #cycles through all newly-infected people, and scans the adjacent 8 cells in their coordinates for susceptibility.
    for i in range(pair[0]-1, pair[0]+2): #+2 rather than +1 to account for exclusivity of last term of range function
      if((i < 0) or (mapLength <= i)):  #if we're scanning a cell that is out of bounds, just skip it and go on.
        continue        
      for j in range(pair[1]-1, pair[1]+2):
        if((j < 0) or (mapWidth <= j)):
          continue 
        if(regionMap[i][j] == 's'):
          #breakpoint()
          if(scanForThreshold(regionMap, i, j, threshold, mapLength, mapWidth, infectionDate, day)):
            regionMap[i][j] = 'i'  #if susceptible, change to infected
            infectionDate[i][j] = day + 1 #technically already infected "tomorrow", before date has been updated
          else:
            continue #TODO: double check to unsure functionality.
  
  #breakpoint()
  regionMap = findRecovered(regionMap, day, infectiousPeriod, infectionDate)

  return regionMap, infectionDate

def simulate(regionMap, threshold, infectiousCount, susceptibleCount, recoveredCount, day, infectionDate, infectiousPeriod):
  mapWidth = len(regionMap[0])
  mapLength = len(regionMap)

  while(infectiousCount[day] != 0):
    print("Day:", day)
    printMap(regionMap)
    regionMap, infectionDate = updateMap(regionMap, threshold, day, infectionDate, mapLength, mapWidth, infectiousPeriod)
    day += 1
    infectiousCount, susceptibleCount, recoveredCount = count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day)
  else:
    print("Day", day)
    printMap(regionMap)
    infectiousCountMaxIndex = infectiousCount.index(max(infectiousCount))
    print("Total population:", (mapWidth*mapLength))
    print("Outbreak Duration:", day, "days")
    print("Peak Day: Day", infectiousCountMaxIndex)
    print("Peak infected count:", infectiousCount[infectiousCountMaxIndex], "people")
    plotEpidemic(infectiousCount, susceptibleCount, recoveredCount, day)
    print("simulation terminated successfully.")
    #TODO: implement descriptors in DOCSTRINGS


def intake(regionMap, infectionDate): #this initializes everything.
  #try:
    fileName = ""
    while(not os.path.exists(fileName)):
      fileName = input("Please input the name of the file which you would like to input for this simulation: ").strip() #intake user input. strip it.

    with open(fileName, 'r') as file: #intake. using "with" to avoid malarkey with file closing
      #handling the first two lines to threshold and infectious period data
      threshold = file.readline()
      threshold = int(threshold.split(":")[1].strip()) #intake line, split string seperated by ":", and then take the second element in the list. strip whitespace.
      infectiousPeriod = file.readline()
      infectiousPeriod = int(infectiousPeriod.split(":")[1].strip())
      for regionLine in file:
        regionLine = regionLine.strip() #Resolved: string are immutable. mutating a string generates a copy that needs to be assigned. I wasn't assigning a copy, hence issues.
        regionLine = regionLine.split(",")

        for value in regionLine: #check if every char in line is a valid health state. if not, break off.
          if (value not in ["s", "i", "r", "v"]):
            raise Exception

        regionMap.append(regionLine)

    day = 0 #initializing day variable
    infectionDate = deepcopy(regionMap) #deepcopying: source: https://stackoverflow.com/questions/68712435/changes-made-in-python-list-showing-up-in-copy-of-original-list
    for rows in range(len(infectionDate)):
      for cols in range(len(infectionDate[rows])):
        if(infectionDate[rows][cols] == 'i'): #check for any day zero patients.
          infectionDate[rows][cols] = day #assign relative coordinate to value '0', indicating day zero infection.
        else:
          infectionDate[rows][cols] = int(threshold)*99 #assign large value so that threshold check will result in negative value, resulting in no change.

    return day, regionMap, threshold, infectiousPeriod, infectionDate
  
  #except Exception:
    print("Invalid health state detected")
    exit(-1)
  #except:
    print("Something went wrong with intake and initialization.")
    exit(-2)
