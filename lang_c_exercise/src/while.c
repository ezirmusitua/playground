#include <stdio.h>
#define ADJUST 7.31

void use_while(void) {
  const double SCALE = 0.333;
  printf("Shoe size (man's)  foot length\n");
  double shoe = 3.0;
  double foot;

  while (shoe < 18.5)
  {
    foot = SCALE * shoe + ADJUST;
    printf("%10.1f %15.2f inches\n", shoe, foot);
    shoe += 1.0f;
  }

  printf("If the shoe fits, wear it. \n");
  return;
}

int main() {
  use_while();
  return 1;
}