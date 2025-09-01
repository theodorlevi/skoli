#!/bin/python

svar = input("breyta tommur í cm: 1\nbreyta cm í tommur: 2\n1, 2: ")

if svar == "1":
  tommur = int(input("sláðu inn tommur: "))
  print("tommur to cm:", round(tommur * 2.54, 2))
else:
  cm = int(input("sláðu inn cm: "))
  print("cm to tommur:", round(cm / 2.54, 2))
