#!/bin/python

tala1 = int(input("sláðu inn tölu 1: "))
tala2 = int(input("sláðu inn tölu 2: "))
tala3 = int(input("sláðu inn tölu 3: "))

if tala1 == tala2 or tala2 == tala3 or tala1 == tala3:
  print("tölur meiga ekki vera eins")
else:
  if tala1 < tala2 and tala1 > tala3:
    print("tala1 er í miðjuni")
  elif tala2 < tala1 and tala2 > tala3:
    print("tala2 er í miðjuni")
  else:
    print("tala3 er í miðjuni")
