#include <stdio.h>

int main() {
  const char *msg = "Don't be a fool!";
  const char *cpy = msg;

  printf("%s\n", cpy);
  printf("msg = %s; &msg = %p; value = %p\n", msg, &msg, msg);
  printf("cpy = %s; &cpy = %p; value = %p\n", cpy, &cpy, cpy);

  return 1;
}