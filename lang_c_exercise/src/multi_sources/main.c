#include <stdio.h>
#include "./source_1.h"
#include "./source_2.h"

int main() {
  printf("Multi-Source Main\n");
  source1_func();
  source2_func();
  return 1;
}