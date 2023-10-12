import pdb
import datetime

#Author: Eugene Kozlakov
#Date: 9/24/2023
#Description: Numerology worksheet.

begin = datetime.datetime.now()

num = 123456789
numStr = str(num) #string variant of num
collector = "" #string -- will append and check divisibility

i = 0 #iterator to iterate through "word" number

#checks permutations and divisibility by force. no fancy bitops unfortunately
while i < len(numStr):
  collector += numStr[i]          #append first digit of number to "collector" var
  remCheck = int(collector)%(i+1) #check for divisibility
  if(remCheck == 0):              #if divisbile by position index, increment i+1 and start next loop
    i += 1
    continue
  else:                           #if not divisible, cycle through other 5 digits. append each and check for divisibility.
    breakpoint()                 #debug
    for j in range(0, len(numStr)):
      if (numStr[j] in collector):#check if every single digit in the original number exists in the collector
        continue                  #if it exists, check the next one

      #if the digit does not exists in the collector, append it and check for divisibility. repeat if not divisible.
      #for the following 3 lines I would like to cite Crowman from Stack overflow.:
      # Link: https://stackoverflow.com/a/18006499

      collectorList = list(collector)
      collectorList[i] = numStr[j]
      collector = "".join(collectorList)
      remCheck = int(collector)%(i+1)

      if(remCheck == 0):
        i += 1
        break
      else: 
        continue

end = datetime.datetime.now()

print("Initial number: %d" % num)
print("Final permutation: %s" % collector)
#print(begin.strftime("%Y-%m-%d %H:%M:%S"))
#print(end.strftime("%Y-%m-%d %H:%M:%S"))




