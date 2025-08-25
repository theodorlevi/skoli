#!/bin/python

einkun = float(input("sláðu inn einkun: "))

if einkun < 0:
  print("óheimil einkun")
if einkun > 10:
  print("óheimil einkun")

elif einkun < 5:
  print("þú féllst")
elif einkun >= 5:
  print("þú féllst ekki")
