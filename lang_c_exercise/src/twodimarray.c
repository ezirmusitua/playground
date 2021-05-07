#include <stdio.h>

int main() {
  printf("Show me the addresses of 2-d array elements\n");

  int two_dim_array[][3] = {{1, 2, 3}, {1, 2, 3}, {1, 2, 3}};

  for (int i = 0; i < 3; i += 1) {
    for (int j = 0; j < 3; j += 1) {
      printf("Value: %d[%p]\n", two_dim_array[i][j], &two_dim_array[i][j]);
    }
  }
  return 1;
}