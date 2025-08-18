#!/bin/python

def main():
    print("input: ", end='')
    n = int(input())

    if n == 0:
      return

    number, iter = full_calculation(n)

    print("largest number:", number, "largest iteration count:", iter)
    return 0

def iteration(start):
    largest = 0;
    iter = 0;

    while start != 1:
        if start % 2 == 0:
            start = start / 2
        else:
            start = start * 3 + 1

        if start > largest:
          largest = start

        iter += 1
    return (largest, iter)

def full_calculation(n):
  largest_number = 0
  largest_iter = 0

  for i in range(1, n):
    number, iter = iteration(i)
    if number > largest_number:
      largest_number = number
    if iter > largest_iter:
      largest_iter = iter
  return (largest_number, largest_iter)

main()
