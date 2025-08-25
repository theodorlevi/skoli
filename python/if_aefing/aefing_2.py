#!/bin/python
mánuðir = [
  "janúar",
  "febrúar",
  "mars",
  "apríl",
  "maí",
  "júní",
  "júlí",
  "ágúst",
  "september",
  "oktober",
  "november",
  "desember",
]


print("mánuðir sem virka")
for mán in mánuðir:
  print(mán, end=', ')

print("\n")

mánuður = input("sláðu inn nafn mánaðar: ")

if mánuður == mánuðir[0]:
  print("1")
elif mánuður == mánuðir[1]:
  print("2")
elif mánuður == mánuðir[2]:
  print("3")
elif mánuður == mánuðir[3]:
  print("4")
elif mánuður == mánuðir[4]:
  print("5")
elif mánuður == mánuðir[5]:
  print("6")
elif mánuður == mánuðir[6]:
  print("7")
elif mánuður == mánuðir[7]:
  print("8")
elif mánuður == mánuðir[8]:
  print("9")
elif mánuður == mánuðir[9]:
  print("10")
elif mánuður == mánuðir[10]:
  print("11")
elif mánuður == mánuðir[11]:
  print("12")
else:
  print("ég þekki ekki þennan mánuð")
