#!/bin/python

stafur = input("sláðu inn sér hljóða eða samhljóða: ")

if stafur[0] == "i" or stafur[0] == "o" or stafur[0] == "u" or stafur[0] == "a" or stafur[0] == "e":
  print("sérhljóði")
elif stafur[0] == "y":
  print("bæði sérhljóði og samhljóði")
else:
  print("samhljóði")
