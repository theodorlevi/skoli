#!/bin/python

def main():
  val = int(input("veldu lið 1 - 6, 7 hætta: "))

  match val:
    case 1:
      flatamal()
    case 2:
      leyni_ord()
    case 3:
      medal_tal()
    case 4:
      hlaup()
    case 5:
      mlitrar()
    case 6:
      margfoldun()
    case 7:
      return 0
  main()
  return 1

# Flatamál
def flatamal():
  lengd: float = float(input("skrifaðu lengd ferhirningsins"))
  breidd: float = float(input("skrifaðu breidd ferhirningsins"))

  print(f"flatamál: {lengd * breidd}")

## Leyniorð
def leyni_ord():
  svar = input("skrifaðu leyni orðið")

  match svar:
    case "leyniorð":
      print("rétt leyni orð")
      return
    case _:
      print("rangt leyiorð reyndu aftur")
      leyni_ord()

### Fimm heiltölur
def medal_tal():
  tolur: list[int] = []
  i = 0

  while i != 5:
    tolur.append(int(input(f"skrifaðu tölu númer {i + 1}: ")))
    i += 1

  heild = 0
  for tala in tolur:
    heild += tala
  print(f"{heild / 5}")

#### Hlaup
def hlaup():
  metrar = int(input("hversu margir metrar hljóp hann: "))

  print(f"hann hljóp: {metrar / 400} 400m hringi")

##### Millilítrar
def mlitrar():
  ml = int(input("hversu margi ml: "))

  print(f"l: {ml / 1000}\ndl: {ml / 100}\nsl: {ml / 10}\nml: {ml}")

###### Margföldun
def margfoldun():
  tala = int(input("skrifaðu tölu til að margfalda: "))

  result: int = tala
  for i in range(tala):
    if i == 0:
      i = 1
    result *= i

  print(result)

exit(main())
