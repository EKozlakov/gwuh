import pdb
import datetime

#Author: Eugene Kozlakov
#Date: 9/24/2023
#Description: Numerology worksheet.
#   +we're gonna have to rewrite this to a heap permutation, possibly. there must be a better algorithm for this.
begin = datetime.datetime.now()

num = 123456789
numStr = str(num) #string variant of num
collector = "" #string -- will append and check divisibility
numList = list(numStr)

rotator = 0 # iterator
divisor = 1
index = 0 #or 'cntr', 'counter'. will look at 'hot seat' digit index, starting count from 0.
swapIndex = 0 #this will follow what digit we should swap the one in the 'hot seat' with
reset = False

while(0 < len(numList)):

  print(collector)


  if(rotator == len(numList)): #rotate i back to start
    rotator = 0

  if (swapIndex == 0):
    collector += numList[rotator]

  if ((int(collector)%divisor) == 0):
    numList.remove(collector[-1])
    swapIndex = 0
    divisor += 1
    index += 1
    continue
  elif(swapIndex == len(numList)): #Failure case: starts permuting all numbers. If we starting with first digit as 1, then being instead with 2, and so on.
    numList = list(numStr)
    divisor = 1
    swapIndex = 0
    index = 0
    rotator += 1 #set to "look" at next digit in the number.
    collector = ""
    continue
  else:
    #breakpoint()
    collectorList = list(collector)
    collectorList[index] = numList[swapIndex]
    collector = "".join(collectorList) # source: https://stackoverflow.com/a/18006499
    swapIndex += 1
    continue    