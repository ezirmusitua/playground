#include <stdio.h>

int main() {

  printf("size of char        : %zd bytes\n", sizeof(char));
  printf("size of short       : %zd bytes\n", sizeof(short));
  printf("size of int         : %zd bytes\n", sizeof(int));
  printf("size of long        : %zd bytes\n", sizeof(long));
  printf("size of long long   : %zd bytes\n", sizeof(long long));
  printf("size of float       : %zd bytes\n", sizeof(float));
  printf("size of double      : %zd bytes\n", sizeof(double));
  printf("size of long double : %zd bytes\n", sizeof(long double));

  return 0;
}