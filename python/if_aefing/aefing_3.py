#!/bin/python

aldur = int(input("sláðu inn aldur: "))

if aldur <= 6 & aldur >= 0:
 print("Nú, svo þú ferð að byrja í skóla")
elif aldur <= 15 & aldur >= 7:
  if input("ætlaru í framhalds skóla, y/n: ") == "y":
    print("(:")
  else:
    print("):")
elif aldur <= 105 & aldur >= 16:
  print("Gangi þér vel í framtíðinni")
else:
  print("þú hefur svarað spurningunni vitlaust")
