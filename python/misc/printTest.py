def printHeaderFooter(borderSelection, size):
  for i in range(size+4): #why +4? honestly, i couldn't tell you. i tried this number and it just starting working from then on.
    print(borderSelection, end="")
  print()#newline


borderSelection = input("please input the border you would like to see: ")

catIMG = []
with open('sailingShip.txt') as f:
  catIMG = f.readlines()


#finds longest row in list, sets that to rowsize.
#partially original code. reference source: 
rowSize = len(max(catIMG, key = len))


printHeaderFooter(borderSelection, rowSize)
#breakpoint()
for row in range(len(catIMG)):
  print(borderSelection, format(catIMG[row].rstrip(), str(rowSize)), borderSelection)

printHeaderFooter(borderSelection, rowSize)



