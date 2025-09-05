#!/bin/python

import random

def main():
  print("1. dkr í isk/isk í dkr\n2. hitastig\n3. reikna margfeldi\n4. kasta teningi\n5. tölur sem enda á 3\n6. dýra dictionary\n7. bekkur og einkunir\n8. spurningar\n9. hætta")
  val = int(input("veldu 1, 9: "))

  match val:
    case 1:
      print(dkr_i_isk(float(input("skráðu inn dkr til að breyta í isk"))))
      print(dkr_i_isk(float(input("skráðu inn isk til að breyta í dkr"))))
    case 2:
      hiti(float(input("skrifaðu hitastig")))
    case 3:
      print(reikna(
        int(input("skrifaðu tölu")),
        int(input("skrifaðu margfeldi tölurnar"))
      ))
    case 4:
      print(kasta(int(input("skrifaðu hversu oft á að kasta"))))
    case 5:
      print(enda_a_3([12, 31, 414, 14, 52, 553, 13], [12, 54, 45, 744, 52, 45, 13, 83, 93]))
    case 6:
      dict1= {"hundar":200, "kettir":120,"fiskar":230}
      dict2= {"kettir":10, "páfuglar":70,"hundar":80}
      print(aminal_dictonry(dict1, dict2))
    case 7:
      bekkur ={"Jón Hallsson":{"STÆR":7,"ENSK":5,"FORR":10, "VERS":8},
                 "Hallur Halldórsson":{"STÆR":2,"ENSK":8,"FORR":9, "VERS":9},
                 "Jóna Jónsdóttir":{"STÆR":3,"ENSK":7,"FORR":5, "VERS":6},
                 "Anna Eiríksdóttir":{"STÆR":10,"ENSK":6,"FORR":1, "VERS":7},
                 "Konráð Vilhjálmsdóttir":{"STÆR":9,"ENSK":5,"FORR":6,"VERS":5},
                 "Gísli Sindrason":{"STÆR":7,"ENSK":7,"FORR":5, "VERS":10},}
      print(medaleinkun_enska_forritun(bekkur))
    case 8:
      spurningar()
    case 9:
      return 0
  main()
  return 1


def dkr_i_isk(isk):
  return isk * 19.13

def isk_i_dkr(dkr):
  return dkr / 19.13

def hiti(hitastig):
  if hitastig <= 10:
    print("Jæja er að koma haust")
  elif hitastig >= 10 & hitastig < 20:
    print("Það er ennþá sumar")
  elif hitastig >= 20:
    munur = hitastig - 20
    if munur <= 8:
      print("Frekar heitt en í góðu lagi. ")
    else:
      print("Þetta hlýtur að vera að völdum loftslagsbreytinga")


def reikna(tala,margfeldi):
  if tala * margfeldi > 100:
    return "Hátala og margfeldistölunni"
  elif tala * margfeldi == 100:
    return "Bingó þetta er talan 100"
  else:
    print("Lítil tala og margfeldistölunni")


def kasta(oft):
  heild = 0
  for _ in range(oft):
    teningur = random.randint(1, 6)

    if teningur == 6:
      teningur = 12

    heild += teningur
  return heild

def enda_a_3(listi1, listi2):
  nyr_listi = []
  for tala in listi1:
    if tala % 10 == 3:
      nyr_listi.append(tala)

  for tala in listi2:
    if tala % 10 == 3:
      nyr_listi.append(tala)

  return nyr_listi

def aminal_dictonry(dict1: dict[str, int], dict2: dict[str, int]):
  nyja_dict = dict1

  for key in dict2:
    value = dict2[key]

    if nyja_dict.get(key) != None:
      nyja_dict[key] = nyja_dict[key] + value
    else:
      nyja_dict[key] = value
  return nyja_dict

def medaleinkun_enska_forritun(bekkur: dict[str, dict[str, int]]):
  meðaleinkun_dict: dict[str, float] = {}
  for nemandi, einkunnir in bekkur.items():
    meðaleinkun_dict[nemandi] = (einkunnir["FORR"] + einkunnir["ENSK"]) / 2

  return meðaleinkun_dict

def spurningar():
  print("a. það er eðlilegra að nota tuple þegar maður þarf ekki að breyta magn hluta í varablinu")
  print("b. box set tekur inn eithvað og skilar öðru")

exit(main())
