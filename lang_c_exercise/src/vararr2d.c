#include <stdio.h>

int sum2d(int rows, int cols, int arr[rows][cols]) {
  int total = 0;
  for (int r = 0; r < rows; r += 1) {
    for (int c = 0; c < cols; c += 1) {
      total += ar[r][c];
    }
  }
  return total;

}

int main() {
  int rs = 3;
  int cs = 4;

  int junk[3][4] = {
    {2, 3, 4, 5},
    {3, 4, 5, 6},
    {4, 5, 6, 7}
  };

  int morejunk[2][6] = {
    {20, 30, 40, 50, 60, 70},
    {5, 6, 7, 8, 9, 10}
  };

  int varr[rs][cs];

  for (int i = 0; i < rs; i += 1) {
    for (int j = 0; j < cs; j += 1) {
      varr[i][j] = i * j + j;
    }
  }

  printf("3x5 array\n");

  printf("Sum of all elements = %d\n", sum2d(2, 6, morejunk));

  printf("3x10 VLA\n");
  printf("Sum of all elements = %d\n", sum2d(rs, cs, varr));

  return 1;
}
