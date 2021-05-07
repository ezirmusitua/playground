#include <stdio.h>
#include <stdbool.h>

int main() {
  printf("Use _Bool type");
  _Bool is_true = 0;
  if (is_true) {
    printf("The _Bool value is true\n");
  } else {
    printf("The _Bool value is false\n");
  }
  bool is_false = true;
  if (is_false) {
    printf("The bool(C99 Standard, #include <stdbool.h>;) value is true\n");
  } else {
    printf("The bool(C99 Standard, #include <stdbool.h>;) value is true\n");
  }
  return 1;
}