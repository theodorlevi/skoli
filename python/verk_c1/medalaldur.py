#!/bin/python

def read(n):
  print("vinsamlegast skrifið aldur nemenda", n, " " , end = '')
  aldur = int(input())
  print("vinsamlegast skrifið nafn nemenda",n, " " , end = '')
  nafn = input()
  return (aldur, nafn)

def procces(nofn, aldrar):
  i = 0
  for nafn in nofn:
    print(nafn, aldrar[i])
    i += 1

  sum_aldrar = 0

  for aldur in aldrar:
    sum_aldrar += aldur

  print("meðal aldurin er:", sum_aldrar / 2) #sloppy fix nenni ekki að debugga meira læri þetta seinna /:


def main():
  reads_aldur = []
  reads_nofn = []
  for i in range(2):
    aldur, nafn = read(i + 1)
    reads_aldur.append(aldur)
    reads_nofn.append(nafn)

  procces(reads_nofn, reads_aldur)

main()
