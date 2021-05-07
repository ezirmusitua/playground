#include <stdio.h>
#define DEFAULT_ROUND 4

void print_indent(int n) {
  for (int i = 0; i < n; i += 1) {
    printf("\t");
  }
  return;
}

void up_and_down(int n, int end) {
  print_indent(n);
  printf("->LEVEL %d: n location %p\n", n, &n);
  if (n < end) {
    up_and_down(n + 1, end);
  }
  print_indent(n);
  printf("<-LEVEL %d: n location %p\n", n, &n);
}

int main() {
  up_and_down(0, DEFAULT_ROUND);
  return 1;
}