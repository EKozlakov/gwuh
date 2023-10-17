targ = 1
ones = [[0,0,0,0,4],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
#locations = list(enumerate(ones))
locations = []
for i in range(len(ones)):
  for j in range(len(ones[i])):
    if (ones[i][j] == targ):
      locations.append([i,j])

#print(locations)
for pair in locations:
  print("Targ Coords (", pair[0], ",", pair[1],")")

print(len(ones[0]))
print(ones[0][4])
#breakpoint()