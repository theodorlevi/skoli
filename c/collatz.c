#include<stdio.h>

typedef struct {
  int iter;
  int number;
} Result;

Result iteration(int start) {
  int iter = 0;
  int largest_num = 0;

  Result result;

  while(start != 1) {
    if(start % 2 == 0) {
      start = start / 2;
    } else {
      start = start * 3 + 1;
    }
    if(start > largest_num) {
      largest_num = start;
    }
    iter += 1;
  }

  result.iter = iter;
  result.number = largest_num;

  return result;
}

Result multiple_iterations(int start) {
  Result largest;

  largest.number = 0;
  largest.iter   = 0;

  while(start != 1) {
    Result iter_result = iteration(start);
    start--;
    if(iter_result.number > largest.number) {
      largest.number = iter_result.number;
    }
    if(iter_result.iter > largest.iter) {
      largest.iter = iter_result.iter;
    }
  }
  return largest;
}

int main() {
  Result result;

  result = multiple_iterations(100000);

  printf("largest number: %d\nlargest iteration: %d", result.number, result.iter);
}
