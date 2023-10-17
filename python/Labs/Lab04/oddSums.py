import random

# Author: Eugene Kozlakov
# Date: 9/24/2023
# Description:  Generates two random integers, and sums all of the odd nums between those two integers.


num1 = random.randint(1, 11) #randnum b/w 1-10
num2 = random.randint(11, 21) #randnum b/w 11-20
binary1 = int(1)
runSum = 0

print(f"Random integer 1: {num1}, Random integer 2: {num2}")
print(format(runSum,">7d"))
for i in range(num1, num2+1):
  if((i & 1) == 0): #initially was i % 2 == 0, but i figured this would be faster/more efficient
    continue
  else:
    print("+",format(i,">5d"))
    runSum += i

print(f"------- \nSum: {runSum}")