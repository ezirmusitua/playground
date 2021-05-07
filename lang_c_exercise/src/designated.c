#include <stdio.h>

int main() {
  int days[6] = {1, 2, 3, [5] = 5, [4] = 4};
  for (int i = 0; i < 6; i += 1) {
    printf("days array element %d: %d[%p], %zd\n", i, days[i], &days[i], sizeof(int));
  }
  return 1;
}