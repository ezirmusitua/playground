#include <stdio.h>

#define SIZE 5

void show_array(const double ar[], int n) {
  for (int i = 0; i < n; i += 1) {
    printf("%8.3f", ar[i]);
  }
  return;
}

void mult_array(double ar[], int n, double mult) {
  for (int i =0; i < n; i+= 1) {
    ar[i] *= mult;
  }
  return;
}

int main() {
  double dip[SIZE] = {20.0, 17.66, 2.33, 1.4, 4.0};

  printf("The original dip array: \n");
  show_array(dip, SIZE);
  mult_array(dip, SIZE, 2.0f);
  printf("\nThe dip array after calling mult_array(): \n");
  show_array(dip, SIZE);

  return 1;
}