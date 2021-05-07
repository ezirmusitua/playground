#include <stdio.h>
#define STLEN 14

int main(void) {
  char words[STLEN];

  puts("Enter a string, please.");
  fgets(words, STLEN, stdin);

  printf("\nYour string twice (puts(), then fputs()):\n");
  puts(words);
  fputs(words, stdout);
  puts("\nEnter another string, please.");

  fgets(words, STLEN, stdin);
  printf("\nYour string twice (puts(), then fputs()):\n");

  puts(words);
  fputs(words, stdout);
  puts("Done.");

  return 0;
}