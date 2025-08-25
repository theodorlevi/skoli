#!/bin/python

tala_1 = float(input("sláðu inn fyrstu tölunna: "))
tala_2 = float(input("sláðu inn seinni tölunna: "))

if tala_1 > tala_2:
  print("fyrsta talan er stærri")
elif tala_2 == tala_1:
  print("tölunar eru jafnar")
else:
  print("seinni talan er stærri")
