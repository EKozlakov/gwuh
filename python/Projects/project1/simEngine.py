import simLibrary as sim

#Author: Eugene Kozlakov
#Date: 10/17/2023
#Description: Base file for simLibrary.py Calls on all files in simLibrary to successfuly execute simulation.


def main():
  """
  Basee file for simulating outbreak. Imports simLibrary as "sim" to execute simulate.

  :param regionMap, type list: This is the list to which the map of the outbreak regioun will be imported from the user-specified input file. Will contain 2D array of health states s, i, r, or v.

  :param susceptibleCount, type list: This is the list which will contain the count of susceptible individuals.

  :param infectiousCount, type list: This is the list which will contain the count of infectious individuals. 

  :param recoveredCount, type list: This is the list which will contain the count of infectious individuals.

  :param infectionDate, type list: This list is a mirror of regionMap. However, instead of containing health states, it will contain integers on each coordinate, indicating date of infection. This map will be used to determined whether an individual has recovered or not.

  :param day, type int: Integer containing day value. Used to track span of simulation and as indexing for _Count[] lists.

  :param threshold, type int: Count of infectious blocks in vicinity of susceptible block needed to successfully infect said susceptbile block.
  """
  regionMap = []
  susceptibleCount = [] # 1D array containing aily count of susceptible individuals. one entry per day.
  infectiousCount = [] # 1D array contianing count of infectious/infected individuals. one entry per day.
  recoveredCount = [] # 1D array containing count of recovered individuals. one entry per day.
  infectionDate = [] # tracking what day each coordinate was infected, if at all. will copy regionMap.
  
  day, regionMap, threshold, infectiousPeriod, infectionDate = sim.intake(regionMap, infectionDate)
  infectiousCount, susceptibleCount, recoveredCount = sim.count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day)
  sim.simulate(regionMap, threshold, infectiousCount, susceptibleCount, recoveredCount, day, infectionDate, infectiousPeriod)

try:
  main()
except:
  print("Something went wrong with the program.")