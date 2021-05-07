#include <stdio.h>

void swap_with_pointer(int *left, int *right) {
  int temp = *left;
  *left = *right;
  *right = temp;
}

void swap_without_pointer(int left, int right) {
  int temp = left;
  left = right;
  right = temp;
}

void print(int left, int right) {
  printf("Left Value: %d, Right Value: %d\n", left, right);
  return;
}

int main() {
  int left = 1;
  int right = 2;
  printf("Initial Value\n\t");
  print(left, right);
  printf("Swap Without Using Pointer\n\t");
  swap_without_pointer(left, right);
  print(left, right);
  printf("Swap With Using Pointer\n\t");
  swap_with_pointer(&left, &right);
  print(left, right);
  return 1;
}