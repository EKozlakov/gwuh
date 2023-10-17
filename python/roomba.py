#name: eugene kozlakov
#date: 9/22/2023


#true == right
#false == left

#assuming start from bottom left
roombaX = 0
roombaY = 0
tilesVisited = 0 #counts number of tiles visited
start = False #startbool

dimX = int(input("Please input an x dimension for your room: "))
dimY = int(input("Please input an y dimension for your room: "))

def clean():
  print("Cleaning!")

def moveForward(direction, dirDim):
  while(direction < dirDim):
    direction +=1

def turn():
  roombaY += 1
  


totalTiles = dimX * dimY

dirtX = 3
dirtY = 5

while(tilesVisited < totalTiles):
#assuming we start moving right
  moveForward(roombaX, dimX)
  turn()
  #moveForward()

