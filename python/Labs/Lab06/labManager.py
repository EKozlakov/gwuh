import pdb

# Author: Eugene Kozlakov
# Date: 10/8/2023
#Description: script that manages lab equipment.

equipmentList = []
userInput = 0
#eqFound = False

print("Welcome to the Lab Equipment Manager!")

while(userInput != 4):
  print("""
  Please select what you would like to do:
    [1] Add Equipment
    [2] Remove Equipment
    [3] Display Current Equipment
    [4] Leave the laboratory manager
  """)
  
  userInput = int(input("Please input integer selection: "))
  
  if(userInput not in range(1, 5)):
    print("Selection not valid. Please try again.")


  if(userInput == 1):
    if(len(equipmentList) == 5):
      print("The Lab has reached its 5-equipment limit. Please remove equipment to add more.")
      continue
    
    #breakpoint()
    eqName = input("Please input the equipment you would like to add: ")
    equipmentList.append(eqName)
    print(f"{eqName} added.")
    continue

  if(userInput == 2):
    if(len(equipmentList) == 0):
      print("There's nothing to remove.")
      continue

    eqName = input("Please input the equipment you would like to remove: ")
    if(eqName in equipmentList):
      print(f"{eqName} has been found. Removing.")
      equipmentList.remove(eqName)
      print(f"{eqName} removed.")
    else:
      print(f"{eqName} not found.")
    continue

  if(userInput == 3):
    print("Currently installed equipment: ")
    for i in range(len(equipmentList)):
      print(f"\t {i+1}) {equipmentList[i]}")
    continue

else:
  print("Thank you for using the Laboratory Equipment Manager! Don't break your new equipment.")

quit()