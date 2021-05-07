#include <stdio.h>
int put2(const char *string)
{
  int count = 0;
  while (*string) /* common idiom       */
  {
    putchar(*string++);
    count++;
  }
  putchar('\n'); /* newline not counted */

  return (count);
}

int main()
{
  put2("my name is  ...");
  return 1;
}