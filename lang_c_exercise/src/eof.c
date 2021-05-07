#include <stdio.h>

int main() {
  char ch;
  printf("enter somehing, enter [EOF] to exit\n");
  while((ch = getchar()) != EOF) {
    printf("input character is: %c\n", ch);
  }
  return 1;
}