import simLibrary as sim

def main():
  regionMap = []
  susceptibleCount = [] # 1D array containing aily count of susceptible individuals. one entry per day.
  infectiousCount = [] # 1D array contianing count of infectious/infected individuals. one entry per day.
  recoveredCount = [] # 1D array containing count of recovered individuals. one entry per day.
  infectionDate = [] # tracking what day each coordinate was infected, if at all. will copy regionMap.
  
  day, regionMap, threshold, infectiousPeriod, infectionDate = sim.intake(regionMap, infectionDate)
  infectiousCount, susceptibleCount, recoveredCount = sim.count(regionMap, infectiousCount, susceptibleCount, recoveredCount, day)
  sim.simulate(regionMap, threshold, infectiousCount, susceptibleCount, recoveredCount, day, infectionDate)

try:
  main()
except:
  print("Something went wrong with the program.")