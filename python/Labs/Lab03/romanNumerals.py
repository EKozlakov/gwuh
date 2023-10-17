decNum = int(input("Please input a number 1-9 that you would like to convert to Roman Numerals: "))

if((decNum > 9) or (decNum < 1)):
  print("You must input a number between 1 and 9!")
elif(decNum == 1):
  print(f"{decNum} is \u2160  as a Roman Numeral.")
elif(decNum == 2):
  print(f"{decNum} is \u2161  as a Roman Numeral.")
elif(decNum == 3):
  print(f"{decNum} is \u2162  as a Roman Numeral.")
elif(decNum == 4):
  print(f"{decNum} is \u2163  as a Roman Numeral.")
elif(decNum == 5):
  print(f"{decNum} is \u2164  as a Roman Numeral.")
elif(decNum == 6):
  print(f"{decNum} is \u2165  as a Roman Numeral.")
elif(decNum == 7):
  print(f"{decNum} is \u2166  as a Roman Numeral.")
elif(decNum == 8):
  print(f"{decNum} is \u2167  as a Roman Numeral.")
elif(decNum == 9):
  print(f"{decNum} is \u2168  as a Roman Numeral.")

#to make this easier, you can just add the decimal number to the unicode val to get your desired roman numeral.