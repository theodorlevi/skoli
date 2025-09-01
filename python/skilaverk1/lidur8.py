#!/bin/python

manudur = int(input("sláðu inn númer mánaðar: "))

if manudur <= 1 and manudur >= 3:
  print("Nú er daginn tekið að lengja.")
elif manudur <= 4 and manudur >= 5:
  print("Vorið er komið og grundirnar gróa.")
elif manudur <= 6 and manudur >= 8:
  print("Núna er sumarið komið með blóm í haga.")
elif manudur <= 9 and manudur >= 10:
  print("Núna er haustið gengið í garð.")
elif manudur <= 11 and manudur >= 12:
  print("Núna styttist í jólin")
else:
  print("Rangur innsláttur")
