#include <stdio.h>

#define PAGES 1067
#define WORDS 65618

void deep_into_prinft(void) {
  printf("*%d*\n", PAGES);
  printf("*%2d*\n", PAGES);
  printf("*%10d*\n", PAGES);
  printf("*%-10d*\n", PAGES);

  const double RENT = -3852.99;
  printf("*%f*\n", RENT);
  printf("*%e*\n", RENT);
  printf("*%4.2f*\n", RENT);
  printf("*%3.1f*\n", RENT);
  printf("*%10.3f*\n", RENT);
  printf("*%10.3E*\n", RENT);
  printf("*%+4.2f*\n", RENT);
  printf("*%010.2f*\n", RENT);

  short num = PAGES;
  short mnum = -PAGES;

  printf("num as short and unsigned short: %hd %hu\n", num, num);
  printf("-num as short and unsigned short: %hd %hu\n", mnum, mnum);
  printf("num as int and char: %d %c\n", mnum, mnum);
  printf("WORDS as int, short, and char: %d %hd %c\n", WORDS, WORDS, WORDS);

  return;
}

int main() {
  deep_into_prinft();
  return 0;
}