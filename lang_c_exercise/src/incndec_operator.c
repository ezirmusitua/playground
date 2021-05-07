#include <stdio.h>

void inc_and_dec() {
  int target = 1;
  printf("current val : %d\n", target);
  printf("pinc: ++i   : %d\n", ++target);
  printf("after pinc  : %d\n", target);
  printf("sinc: i++   : %d\n", target++);
  printf("after sinc  : %d\n", target);
  printf("pdec: --i   : %d\n", --target);
  printf("after pdec  : %d\n", target);
  printf("sinc: i--   : %d\n", target--);
  printf("after sdec  : %d\n", target);
  return;
}

int main() {
  inc_and_dec();
  return 1;
}