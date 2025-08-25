#!/bin/python

tala = int(input("sláðu inn tölu frá 0 - 25: "))

if tala < 0:
  print("Rangur innsláttur")
elif tala > 25:
  print("Rangur innsláttur")
else:
  print(tala * 1.7)
