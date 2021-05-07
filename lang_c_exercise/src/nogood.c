#include <stdio.h>
#include <stdint.h>

int main() {
  uint32_t n = 5;
  uint32_t n1 = n * n;
  uint32_t n2 = n1 * n1;

  printf("n = %d, n^2 = %d, n^4 = %d\n", n, n1, n2);

  return 0; 
}