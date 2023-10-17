import matplotlib.pyplot as plotty
import random
import pdb
# Author: Eugene Kozlakov
# Date: 10/8/2023
# Description: script that generates and plots random temperatures of cities.

time = list(range(1,13)) # generates a list of nums
LosAngeles = []
NewYork = []
WolfCreek = [] #montana

for i in range(len(time)):
  #breakpoint()
  LosAngeles.append(random.randint(10,30))
  NewYork.append(random.randint(10,30))
  WolfCreek.append(random.randint(10,30))

plotty.plot(time, LosAngeles, marker='o', label = "Los Angeles, CA")
plotty.plot(time, NewYork, marker = '^', label = "New York City, NY")
plotty.plot(time, WolfCreek, marker = 's', label = "Wolf Creek, MT")
plotty.legend(loc="upper right")
plotty.grid(which = "both", axis = "both")

plotty.title("Tempuratures in Various Cities over Time")
plotty.xlabel("Time")
plotty.ylabel("Temp, Celsius")

plotty.show()