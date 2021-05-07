#include <stdio.h>

int sum(const int ar[], int n) {
  int total = 0;
  for (int i = 0; i < n; i += 1) {
    total += ar[i];
  }
  return total;
}

int sum2d(int rows, int cols, const int ar[rows][cols]) {
  int total = 0;
  for (int i = 0; i < rows; i += 1) {
    for (int j = 0; j < cols; j += 1) {
      total += ar[i][j];
    }
  }
  return total;
}

int main() {
  int *pt1 = (int [2]){10, 20};
  int (*pt2)[3] = (int [2][3]){
    {1, 2, 3},
    {1, 2, 3},
  };
  printf("total 1: %d\n", sum((int []) {1, 2, 3, 4, 5}, 5));
  printf("total 2: %d\n", sum(pt1, 2));
  printf("total 3: %d\n", sum2d(2, 3, pt2));
  return 1;
}