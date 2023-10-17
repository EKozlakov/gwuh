import math

def dA(H):
  return 2*math.sqrt((8/3)*H)+7

def dB(H):
  return 4*math.sqrt((10/3)*H)+5

def dC(H):
  return 4*math.sqrt((5/3)*H)+5

def dD(H):
  return 8*(((10/3)*H)**0.25)+7

#Hvals = [1, 5, 20]
Heq1 = []
Heq5 = []
heq20 = []

Heq1 = [dA(1), dB(1), dC(1), dD(1)] 
Heq5 = [dA(5), dB(5), dC(5), dD(5)]
Heq20 = [dA(20), dB(20), dC(20), dD(20)]

print(" Delays for H = 1 ", Heq1)
print(" Delays for H = 5 ", Heq5)

print(" Delays for H = 20 ", Heq20)