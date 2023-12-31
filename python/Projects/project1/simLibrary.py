import matplotlib.pyplot as plt
import os
import pdb
from copy import deepcopy #imported because it turns out python list.copy function only makes a shallow copy that maintains all ref pointers. this screwed with my functionality.
# Author: Eugene Kozlakov
# Date: 10/15/2023
# Description: Library for SimEngine.py to execute a simualation of disease spread.

def count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day): #runs a count of all peoples, with day being index. presumes indexing is reliable.
  """
  A function used to count the number of susceptible, infectious, and recovered individuals each day.

  Algorithim/Methodology:
    1. Intakes the regionMap, lists for counting the S, I, and V populations, and the simulation day.
    2. Assumes the "day" is the next index of the list that needs to be added.
    3. Appends zeroes to all three lists.
    4. Scans map, increments list depending what health state is present in each cell at index "day". If vaccinated, skip.
    5. Returns all three lists containing counts for new day.

  Intake Parameters:
    :param susceptibleCount, type list: This is the list which will contain the count of susceptible individuals.

    :param infectiousCount, type list: This is the list which will contain the count of infectious individuals. 

    :param recoveredCount, type list: This is the list which will contain the count of infectious individuals.

    :param day, type int: Current day of epidemic

  Return Parameters:
    None.

  """
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
  A function to print out the regionMap. Used for visualization.
  
  Intake parameters:
    :param map, type List: 2D map of region in current state.

  Intermediate parameters:
    :param endSeq, type string: String to indicate the end of a colored ASCII block sequence. Used to "officially" turn off terminal coloring using ASCII.

    :param redSeq, type string: String containing ASCII escape sequence to make background red for map visualization. (infected cells)

    :param yelSeq, type string: String containing ASCII escape sequence to make background yellow for map visualization. (susceptible cells)

    :param greSeq, type string: String containing ASCII escape sequence to make background green for map visualization. (recovered cells)

    :param bluSeq, type string: String containing ASCII escape sequence to make background blue for map visualization. (vaccinated cells)

  Return parameters:
    None

  Algorithm/Methodology:
    1. Intake map (this is assumed to be the regionMap)
    2. Scan map
    3. Check cell
      -if infected, print red
      -if susceptible, print yellw
      -if recovered, print green
      -if vaccinated print blue/cyan
    4. Once map scanned and printed to terminal, leave

  Note: When colors are painted in the terminal, and the terminal window is resized, you get some of the row colors "running" off
  to the edge of the screen. This is supposedly an old issue that has only recently been fixed in Windows Terminal (please see: 
  https://github.com/microsoft/terminal/pull/12637), but as far as I can tell this has not reached other terminals yet -- at least,
  it hasn't reached mine. Just be wary of these issues as it can make the coloring of the cells look VERY ugly.

  Source for ANSII escape chars: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
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
  """
  A function that finds the coordinates of cells that find all people that have been infected "today", so that we can know who "will" be infected "tomorrow."
  Reutrns a list of coordinate pairs for regionMap. 

  Intake parameters:
    :param infectionDate, type List: 2D list containing the integer day-of-infection of at each specific coordinate. 

    :param day, type int: Day of simulation, to check in infectionDate param which cells have been infected "today." These correspond to identical locations on the regionMap.

  Return Parameters:
    :param locations, type List: list of pair integers (row,column) indicating the locations of the latest infected cells.
  """

  locations = []
  for i in range(len(infectionDate)):
    for j in range(len(infectionDate[i])):
        if(infectionDate[i][j] == day):
          locations.append([i,j])
  return locations

def findRecovered(regionMap, day, infectiousPeriod, infectionDate): #checks day of infection, infectionMap, and checks cells for passed threshold time.
  """
  Function that locates all cells that can be marked as "recovered" for the next day.
  Compares day with each coordinate's date of infection in "infectionDate" map. 
  If the comparison is greater than or equal to the infectious period, update cell to recovered.

  Intake parameters:
    :param regionMap, type List: Two dimensional list containing map of all health states.

    :param day, type int: Current day of epidemic

    :param infectiousPeriod, type int: Integer indicating how long each cell is to be infected.

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

  Return paremters:
    :param regionMap, type List: modified so it contains new recovered cells.
  """
  for i in range(len(infectionDate)):
    for j in range(len(infectionDate[i])):
        if(infectiousPeriod <= ((day+1) - infectionDate[i][j])): #because we are doing these updates "overnight", we have to account for what will happen "tomorrow." Therefore, we need to act as if we tallying day of, before printing -- like at "midnight updates."
          regionMap[i][j] = 'r'
  return regionMap

def plotEpidemic(infectiousCount, susceptibleCount, recoveredCount, day):
  """
  Function that plots epidemic statistics using matplotlib. Plots all counts of infectious, susceptible, and recovered cells over time from Day 0 to the current Day value.

  Intake paramters:
    :param susceptibleCount, type list: This is the list which will contain the count of susceptible individuals.

    :param infectiousCount, type list: This is the list which will contain the count of infectious individuals. 

    :param recoveredCount, type list: This is the list which will contain the count of infectious individuals.

  Return parameters:
    None.

  Notes:
    Y-axis data:
      infectiousCount
      susceptibleCount
      recoveredCount
    X-Axis data:
      day
  """
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
  """
  Function that scans cells around a given susceptible cell to check if it meets threshold for infection.

  Intake Parameters:
    :param regionMap, type List: Two dimensional list containing map of all health states.

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

    :param row, type int: Row coordinate of susceptible cell at center of scan

    :param col, type int: Column coordinate of susceptible cell at center of scan

    :param threshold, type int: Count of infectious blocks in vicinity of susceptible block needed to successfully infect said susceptbile block.

    :param mapLength, type int: "Length" (y-axis dimension) of regionMap

    :param mapWidth, type int: "Width" (x-axis dimension) of regionMap

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

    :param day, type int: Current day of epidemic

  Intermediate paramters:

    :param iCounter, type int: Counter that tracks number of infected cells surrounding susceptible cell.

  Return parameters:

    :param [boolean]: returns true if number of infected cells surrounding susceptible cell is greater than or equal to the threshold. Otherwise, return false.
  """
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

  return False

def updateMap(regionMap, threshold, day, infectionDate, mapLength, mapWidth, infectiousPeriod):
  """
  Function that is the primary for keeping map updated.

  Algorithm Explanation:
    1) After finding all currently infected cells using findInfected(), 
    2) We visit each coordinate in the list returned by the function findInfected()
    3) Check if any of the adjacent cells (3x3 area) for each pair meet threshold for infection using scanForThreshold()
    4) If met, change the cell we are lookig from 'susceptible' to infected. If not, move to next infected coordinate.
    5) Find any and all cells eligible to marked as "recovered."
    6) Return updated infectionDate and regionMap arrays to simulate() function below


  Intake Parameters:
    :param regionMap, type List: Two dimensional list containing map of all health states.
    
    :param threshold, type int: Count of infectious blocks in vicinity of susceptible block needed to successfully infect said susceptbile block.

    :param day, type int: Current day of epidemic

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

    :param mapLength, type int: "Length" (y-axis dimension) of regionMap

    :param mapWidth, type int: "Width" (x-axis dimension) of regionMap

    :param infectiousPeriod, type int: Integer indicating how long each cell is to be infected.

  return parameters:
    :param regionMap, type List: Two dimensional list containing map of all health states.

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

  """
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
            continue 
  
  #breakpoint()
  regionMap = findRecovered(regionMap, day, infectiousPeriod, infectionDate)

  return regionMap, infectionDate

def simulate(regionMap, threshold, infectiousCount, susceptibleCount, recoveredCount, day, infectionDate, infectiousPeriod):
  """
  Simulation driving function.

  Algorithm:
    While there are infected people in the region:
    1) Print the current day, region, and health states of region.
    2) Send appropriate variables to updateMap() to proceed with simulation.
    3) Increment Day
    4) Make new counts of infected, susceptible, recovered, etc.
    5) Continue until there are no more infected people in the region.
    When there are no more infected people:
    1) Print final day, map, and healthstates in region.
    2) Find days of peak of epidemic, peak infected counts, and druation of outbreak. Print the results
    3) Plot the counts of susceptible, infected, and recovered people over the course of the epidemic. Exit.

  Intake Parameters:
    :param regionMap, type List: Two dimensional list containing map of all health states.
    
    :param threshold, type int: Count of infectious blocks in vicinity of susceptible block needed to successfully infect said susceptbile block.
    
    :param susceptibleCount, type list: This is the list which will contain the count of susceptible individuals.

    :param infectiousCount, type list: This is the list which will contain the count of infectious individuals. 

    :param recoveredCount, type list: This is the list which will contain the count of infectious individuals.

    :param day, type int: Current day of epidemic

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

    :param infectiousPeriod, type int: Integer indicating how long each cell is to be infected.
  """
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


def intake(regionMap, infectionDate): #this initializes everything.
  """
  Function that initializes lists and variables needed for simulation. Extracts data from user input file.
  If any health states that are read are invalid, throws exception.
  If anything goes wrong during intake, throws exception.

  Intake parameters:
    :param regionMap, type List: Two dimensional list containing map of all health states.

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

  Intermediate Parameters:
    :param fileName, type string: Name of file user would like to use. Set to blank by default so it fails existence check by default.

    :param regionLine, type string, list: String that is then rewritten as a list via split(","), using comma as delimiter to create elements to map to regionMap.

    :param file, type fileObject: File Object used to navigate user input file.

  Return Parameters:
    :param day, type int: Will be used to track day of epidemic. In this function, always returned as zero, but can be theoretically modified to something else.

    :param regionMap, type List: Two dimensional list containing map of all health states.

    :param threshold, type int: Count of infectious blocks in vicinity of susceptible block needed to successfully infect said susceptbile block.

    :param infectionDate, type List: 2D List with the date of infection on each coordinate.

    :param infectiousPeriod, type int: Integer indicating how long each cell is to be infected.

  """
  try:
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
        regionLine = regionLine.strip() #Recopying string to sidestep string immutability
        regionLine = regionLine.split(",") #split the lines via "," delimiter

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
          infectionDate[rows][cols] = int(infectiousPeriod)*99 #assign large value so that threshold check will result in negative value, resulting in no change. This is kind of janky, but it works for now.

    return day, regionMap, threshold, infectiousPeriod, infectionDate
  
  except Exception:
    print("Invalid health state detected")
    exit(-1)
  except:
    print("Something went wrong with intake and initialization.")
    exit(-2)
  
