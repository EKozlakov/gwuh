import random
import itertools

#Author: Eugene Kozlakov
#Date: 10/18/2023 10/19/2023
#Description: Generates an input file for epidemic simulator. 

def printMap(area): #mainly for debug
  """
  This is a function to print out the array to denote the map.
  Returns nothing.

  Intake Parameters:
    :param area, type list: A 2-Dimensional list of any kind.

  Output Parameters:
    :return: none.

  Intermediate Parameters:
    none.
  """
  for i in range(len(area)):
    for j in range(len(area[i])):
      print(area[i][j], end = " ")
    print()#newline

def fileGen():

  """
  A function that generates an input file for simEngine.py and simLibrary.py.

  Intake Parameters:
    None.

  Output Parameters:
    None. Creates file in relative directory based on user input.

  Intermediate Parameters:
    :param mapLength, string-cast-to-int: User input dimensioned for desired "length" (y-axis dimension) of graph.

    :param mapWidth, string-cast-to-int: User input dimensioned for desired "width" (x-axis dimension) of graph. 

    :param population, type int: Total number of "people" in the map. Found by multiplying mapLength*mapWidth

    :infectiousQuantity, type int: Population of infectious people. User input value.

    :vaccinatedQuantity, type int: Population of vaccinated people. User input value.

    :susceptibleQuantity, type int: Population of susceptible people. Calculated by the following formula:
      susceptibleQuantity = population - (vaccinatedQuantity + infectiousQuantity). Initialized to negative one
      for flow control reasons. Elaboration in algorithm breakdown.
    
    :infectiousPeriod, type int: Duration, how long a cell stays infected. User input value.

    :threshold, type int: The value for how many infected cells need to be surrounding a susceptible cell 
      for it to be "successfully" infected. User input value.
    
    :filename, type string: The user-input name for their generated input file.

    :mapTemp, type List: The 2D list containing the region map of the whole population. Will be written to .txt file.

    :delList, type List: List of coordinate pairs to remove for each occupied position in mapTemp. Assissts in random assignment of
      vaccinated/infectious populations -- does not rely on randomly choosing.
    
    :coords, type List: a List containing coordinates for every single cell in the map. Accelerates random selection of coordinates
      and preventing overlap.

    ALGORITHM BREAKDOWN:
      1. User is prompted for the following parameters:
          i) mapLength (y-axis dimensions)
         ii) mapWidth (x-axis dimensions)
              - population is calculated here
        iii) infectiousQuantity
         iv) vaccinatedQuantity
              -susceptibleQuantity is calculated here
          v) infectiousPeriod
         vi) thershold
        vii) filename

      2. We initiate the map to store the "coordinates" for each cell on the map.
          This will help us write to the file from the map later down the line.
      
      3. We use itertools.permute() to generate coordinate pair based on the size
          of the map. Since, itertools.permute() does not generate pairs that contain
          duplicates (0,0), (1,1), (2,2), (3,3), etc., we have to add them ourselves
          via an appending for loop.

      4. We then generate coordinate pairs in a square based on the largest dimension provided;
          we then remove the coordinates that have positions out of bounds. We accomplish this
          by finding the axis with the smallest dimensions, and then eliminating coordinates
          larger than that dimension in that axis.

      5. Now that we have a valid set of coordinates, we assign vaccinated and infectious individuals
          at random by randomly selecting a pair from the coords[] list. For each individual assigned
          from these groups, we substract from the user-input counts until they are equal to zero.
          These are split into two seperate while-loops.

      6. Once both vaccinated and infectious individuals are assigned,we assign the rest of the positions
          to susceptible individuals, iterating through each position on the map. We skip positions where
          infectious or vaccinated individuals have been previously assigned.

      7. We then write to the target file all necessary details. This means the threshold, infectious
          period while also writing to the file from the previously-laid-out "mapTemp" array/list/map.

      8. File produced and process finished.
  
  """

  print("File Generator")

  mapLength = int(input("Please input the length (y-axis dimension) of the region map you would like to have: "))
  mapWidth = int(input("Please input the width (x-axis dimension) of the region map you would like to have: "))
  population = mapLength*mapWidth

  susceptibleQuantity = -1
  while(susceptibleQuantity < 0):
    infectiousQuantity = int(input("Please input the number of infectious people you would like to have in your population: "))
    vaccinatedQuantity = int(input("please input the number of vaccinated people you would like in your population: "))
    susceptibleQuantity = population - (infectiousQuantity + vaccinatedQuantity)
    if(susceptibleQuantity < 0):
      print(f"Infected population ({infectiousQuantity}) and Vaccinated population ({vaccinatedQuantity}) in total ({infectiousQuantity} + {vaccinatedQuantity} = {vaccinatedQuantity+infectiousQuantity}) exceed overall population ({population}). Please try another number.")
      continue

  infectiousPeriod = input("Please input the infectious period for your simulation: ").strip() #.strip() to clean up inputs
  threshold = input("Please input the threshold you would like to have for your simulation: ").strip()
  fileName = input("Please input the title you would like for your file. The \".txt\" suffix will be appended automatically: ").strip()
  fileName = fileName + ".txt"

  
  mapTemp = [[ "O" for i in range(mapWidth)] for j in range(mapLength)]
  delList = [] #list which will contain coords to be deleted
  
  #the following was done because a previous version of my algorithm, using x = rand(mapWidth), y = rand(mapLength), was simply stuck in an infinite
  #loop trying to choose the last two coordinates. this increases the speed of coordinate selection by a bunch (didnt measure), and works destructively
  #rather than constructively. large memory cost up front, but eliminate a lost of hassle from trying to randomly select stuff.
  
  if(mapLength > mapWidth): #using itertools source: https://stackoverflow.com/questions/5360220/how-to-split-a-list-into-pairs-in-all-possible-ways
    coords = list(itertools.permutations(range(mapLength), 2))
    for i in range(mapLength): #this loop is to account for itertools not creating coordinate pairs containing duplicate vals, i.e. (0,0), (1,1), etc.
      coords.append((i,i))
    for pair in coords:
      if pair[1] > (mapWidth-1):
        
        delList.append(pair) #remove used coordinate pair, so that there are no overlaps. appended to seperate list to avoid "index skipping" from removal
    #delListCopy = [pair for pair in coords if pair[1] > (mapWidth - 1)] #for some reason, this results in a blank list. Any help?
  elif(mapLength < mapWidth):
    coords = list(itertools.permutations(range(mapWidth), 2))
    for i in range(mapLength):
      coords.append((i,i))
    for pair in coords:
      if pair[0] > (mapLength-1): #clearing out all permutes that are out of bounds for graph
        delList.append(pair)
    #delListCopy = [pair for pair in coords if (pair[1] > (mapWidth - 1))] #for some reason, this results in a blank list. not sure why.
  else:
    coords = list(itertools.permutations(range(mapWidth), 2)) #removal not needed, this would be the situation where map is a square

  
  coords = [pair for pair in coords if pair not in delList] # Logically: coords = coords - delList #source for this line: https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another


  while(0 < vaccinatedQuantity):
    pair = random.choice(coords)
    
    mapTemp[pair[0]][pair[1]] = "v"
    coords.remove(pair)
    vaccinatedQuantity -= 1
  
  while(0 < infectiousQuantity):
    pair = random.choice(coords)
    mapTemp[pair[0]][pair[1]] = "i"
    coords.remove(pair)
    infectiousQuantity -= 1
  
  for i in range(mapLength):
    for j in range(mapWidth):
      if((mapTemp[i][j] == "i") or (mapTemp[i][j] == "v")):
        continue
      mapTemp[i][j] = "s"
  
  with open(fileName, 'a') as file:
    file.write("Threshold:" + threshold + "\n")
    file.write("Infectious Period:" + infectiousPeriod + "\n")

    for i in range(len(mapTemp)):
      for j in range(len(mapTemp[i])):
        if(j == (mapWidth - 1)):
          file.write(mapTemp[i][j] + "\n")
        else:
          file.write(mapTemp[i][j] + ",")

def main():
  fileGen()

main()