import os
import pdb
import traceback #source: https://stackoverflow.com/questions/3702675/catch-and-print-full-python-exception-traceback-without-halting-exiting-the-prog
from copy import deepcopy #imported because it turns out python list.copy function only makes a shallow copy that maintains all ref pointers. this screwed with my functionality.
# Author: Eugene Kozlakov
# Date: 10/15/2023
# Description: Program that uses simLibrary.py to execute a simualation of disease spread.

def count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day): #runs a count of all peoples, with day being index.
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



def printMap(map, day): #prints map.
  print("Day:", day)

  for rows in range(len(map)):   
    for cols in range(len(map[rows])):
      print(map[rows][cols], end=" ")
    print() #newline

def findInfected(infectionDate, day): #find all that are infected on current day. this will help in finding all adjacent cells to be infected "tomorrow"
  locations = []
  for i in range(len(infectionDate)):
    for j in range(len(infectionDate[i])):
        if(infectionDate[i][j] == day):
          locations.append([i,j])
  return locations

def findRecovered(regionMap, day, threshold, infectionDate):
  for i in range(len(infectionDate)):
    for j in range(len(infectionDate[i])):
        #breakpoint()
        if(threshold <= (day - infectionDate[i][j])):
          regionMap[i][j] = 'r'
  return regionMap

def updateMap(regionMap, threshold, day, infectionDate):
  currentInfected = []
  currentInfected  = findInfected(infectionDate, day) #successfully passes back coordinates.
  mapWidth = len(regionMap[0])
  mapLength = len(regionMap)

  #breakpoint()
  for pair in currentInfected: #cycles through all newly-infected people, and scans the adjacent 8 cells in their coordinates for susceptibility.
    for i in range(pair[0]-1, pair[0]+2): #+2 rather than +1 to account for exclusivity of last term of range function
      if((pair[0]-1 < 0) or (mapLength <= pair[0]+1 )):
        continue        
      for j in range(pair[1]-1, pair[1]+2):
        if((pair[1]-1 < 0) or (mapWidth <= pair[1]+1 )):
          continue 
        if(regionMap[i][j] == 's'):
          regionMap[i][j] = 'i'
          infectionDate[i][j] = day + 1 #technically already infected "tomorrow", before date has been updated
  
  regionMap = findRecovered(regionMap, day, threshold, infectionDate)

  return regionMap, infectionDate


def simulate(regionMap, threshold, infectiousCount, susceptibleCount, recoveredCount, day, infectionDate):

  while(infectiousCount[day] != 0):
    printMap(regionMap, day)
    regionMap, infectionDate = updateMap(regionMap, threshold, day, infectionDate)
    day += 1
    infectiousCount, susceptibleCount, recoveredCount = count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day)
    #breakpoint()
  else:
    printMap(regionMap, day)
    infectiousCountMaxIndex = infectiousCount.index(max(infectiousCount))
    print("Peak Day:", infectiousCountMaxIndex)
    print("Peak infected count:", infectiousCount[infectiousCountMaxIndex])
    print("simulation terminated successfully.")
    #TODO: implement plots from MATPLOTLIB
    #TODO: implement descriptors in DOCSTRINGS


def intake(regionMap, infectionDate): #this initializes everything.
  fileName = input("Please input the name of the file which you would like to input for this simulation: ") #intake user input

  with open(fileName, 'r') as file: #intake. using "with" to avoid malarkey with file closing
    #handling the first two lines to threshold and infectious period data
    threshold = file.readline()
    #breakpoint()
    threshold = int(threshold.split(":")[1].strip()) #intake line, split string seperated by ":", and then take the second element in the list. strip whitespace.
    #print("Threshold: ", threshold)
    infectiousPeriod = file.readline()
    infectiousPeriod = infectiousPeriod.split(":")[1].strip()
    #print("Inefction Period: ", infectiousPeriod)
    #breakpoint()
    for regionLine in file:
      regionLine = regionLine.strip() #Resolved: string are immutable. mutating a string generates a copy that needs to be assigned. I wasn't assigning a copy, hence issues.
      regionLine = regionLine.split(",")

      for value in regionLine: #check if every char in line is a valid health state. if not, break off.
        if (value not in ["s", "i", "r", "v"]):
          raise Exception("Invalid health state detected")
        
      regionMap.append(regionLine)
        
  day = 0 #initializing day variable
  infectionDate = deepcopy(regionMap) #deepcopying: source: https://stackoverflow.com/questions/68712435/changes-made-in-python-list-showing-up-in-copy-of-original-list
  #breakpoint()
  for rows in range(len(infectionDate)):
    for cols in range(len(infectionDate[rows])):
      if(infectionDate[rows][cols] == 'i'): #check for any day zero patients.
        infectionDate[rows][cols] = day #assign relative coordinate to value '0', indicating day zero infection.
      else:
        infectionDate[rows][cols] = int(threshold)*99 #assign large value so that threshold check will result in negative value, resulting in no change.
  #breakpoint()

  return day, regionMap, threshold, infectiousPeriod, infectionDate

def main():

  regionMap = []
  susceptibleCount = [] # 1D array containing aily count of susceptible individuals. one entry per day.
  infectiousCount = [] # 1D array contianing count of infectious/infected individuals. one entry per day.
  recoveredCount = []# 1D array containing count of recovered individuals. one entry per day.
  infectionDate = [] #tracking what day each coordinate was infected, if at all. will copy regionMap.
  #A PERSON'S COORDINATES WILL SERVE AS THEIR IDENTITY
  day, regionMap, threshold, infectiousPeriod, infectionDate = intake(regionMap, infectionDate)
  infectiousCount, susceptibleCount, recoveredCount = count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day)
  #breakpoint()
  print(threshold)
  print(infectiousPeriod)
  print(regionMap)
  print(day)
  simulate(regionMap, threshold, infectiousCount, susceptibleCount, recoveredCount, day, infectionDate)




main()