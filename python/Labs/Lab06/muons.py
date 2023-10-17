import random
DIM = 8 # CONSTANT dimension for map/sensor/array size.


# Author: Eugene Kozlakov
# Date: 10/8/2023
# Description: script that simulates CRMD particle detector.

arrayList = []
hiCapRow = 0 #highest capture rate, X-value
hiCapCol = 0 #highest capture rate, Y-value
hiCapVal = -1 
loCapRow = 0 #lowest capture rate, X-value
loCapCol = 0 #lowest capture rate, Y-value
loCapVal = 999

for i in range(DIM):
  arrayList += [[0]*DIM]

print("Generating CRMD Simulation\n")

for i in range(DIM):
  for j in range(DIM):
    arrayList[i][j] = random.randint(0,500)
    if(arrayList[i][j] > hiCapVal):
      hiCapVal = arrayList[i][j]
      hiCapRow = i + 1
      hiCapCol = j + 1
    if(arrayList[i][j] < loCapVal):
      loCapVal = arrayList[i][j]
      loCapRow = i + 1
      loCapCol = j + 1

#printing
#setting up x and y coordinate indicators.
print(end = "  ")
for index in range(DIM):
  print(format(index+1, '>3d'), end = " ")

print()
print(end = "  ") 
for index in range(DIM*4):
  print("=", end = "")

print() #newline
for i in range(DIM):
  print (i + 1,"|",end = "")
  for j in range(DIM):
    print(format(arrayList[i][j], '>3d'), end=" ")
  print()

print(f"""
Highest Captured Value: {hiCapVal}, coordinates: ({hiCapCol}, {hiCapRow})
Lowest Captured Value: {loCapVal}, coordinates: ({loCapCol}, {loCapRow})
""")