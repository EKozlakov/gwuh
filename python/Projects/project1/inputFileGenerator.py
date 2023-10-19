import random
import itertools

def printMap(area): #mainly for debug
  for i in range(len(area)):
    for j in range(len(area[i])):
      print(area[i][j], end = " ")
    print()#newline

def fileGen():

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

  infectiousPeriod = input("Please input the infectious period for your simulation: ").strip()
  threshold = input("Please input the threshold you would like to have for your simulation: ").strip()
  fileName = input("Please input the title you would like for your file. The \".txt\" suffix will be appended automatically: ").strip()
  fileName = fileName + ".txt"

  #breakpoint()
  mapTemp = [[ "O" for i in range(mapWidth)] for j in range(mapLength)]
  delList = [] #list which will contain coords to be deleted
  
  #the following was done because a previous version of my algorithm, using x = rand(mapWidth), y = rand(mapLength), was simply stuck in an infinite
  #loop trying to choose the last two coordinates. this increases the speed of coordinate selection by a bunch (didnt measure), and works destructively
  #rather than constructively. large memory cost up front, but eliminate a lost of hassle from trying to randomly select stuff.
  #breakpoint()
  if(mapLength > mapWidth): #using itertools source: https://stackoverflow.com/questions/5360220/how-to-split-a-list-into-pairs-in-all-possible-ways
    coords = list(itertools.permutations(range(mapLength), 2))
    for i in range(mapLength): #this loop is to account for itertools not creating coordinate pairs containing duplicate vals, i.e. (0,0), (1,1), etc.
      coords.append((i,i))
    for pair in coords:
      if pair[1] > (mapWidth-1):
        #breakpoint()
        delList.append(pair) #remove used coordinate pair, so that there are no overlaps. appended to seperate list to avoid "index skipping" from removal
    #delListCopy = [pair for pair in coords if pair[1] > (mapWidth - 1)] #for some reason, this results in a blank list.
    #breakpoint()
  elif(mapLength < mapWidth):
    coords = list(itertools.permutations(range(mapWidth), 2))
    for i in range(mapLength):
      coords.append((i,i))
    for pair in coords:
      if pair[0] > (mapLength-1): #clearing out all permutes that are out of bounds for graph
        delList.append(pair)
    #breakpoint()
    #delListCopy = [pair for pair in coords if (pair[1] > (mapWidth - 1))] #for some reason, this results in a blank list. not sure why.
  else:
    coords = list(itertools.permutations(range(mapWidth), 2)) #removal not needed, this would be the situation where map is a square

  #breakpoint()
  coords = [pair for pair in coords if pair not in delList] # Logically: coords = coords - delList #source for this line: https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another


  #breakpoint()
  while(0 < vaccinatedQuantity):
    pair = random.choice(coords)
    #breakpoint()
    mapTemp[pair[0]][pair[1]] = "v"
    coords.remove(pair)
    vaccinatedQuantity -= 1

  #breakpoint()
  while(0 < infectiousQuantity):
    pair = random.choice(coords)
    mapTemp[pair[0]][pair[1]] = "i"
    coords.remove(pair)
    infectiousQuantity -= 1

  #printMap(mapTemp)
  
  #breakpoint()
  for i in range(mapLength):
    for j in range(mapWidth):
      if((mapTemp[i][j] == "i") or (mapTemp[i][j] == "v")):
        continue
      mapTemp[i][j] = "s"
  
  printMap(mapTemp)

  #breakpoint()
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