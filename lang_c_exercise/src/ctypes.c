#include <stdio.h>
#include <ctype.h>

int main()
{
  /**
 * __exctype (isalnum);
 * __exctype (isalpha);
 * __exctype (iscntrl);
 * __exctype (isdigit);
 * __exctype (islower);
 * __exctype (isgraph);
 * __exctype (isprint);
 * __exctype (ispunct);
 * __exctype (isspace);
 * __exctype (isupper);
 * __exctype (isxdigit);
 **/
  printf("1 isalnum or not      : %d\n", isalnum('1'));
  printf("1 isalpha or not      : %d\n", isalpha('1'));
  printf("1 iscntrl or not      : %d\n", iscntrl('1'));
  printf("1 isdigit or not      : %d\n", isdigit('1'));
  printf("1 islower or not      : %d\n", islower('1'));
  printf("1 isgraph or not      : %d\n", isgraph('1'));
  printf("1 isprint or not      : %d\n", isprint('1'));
  printf("1 ispunct or not      : %d\n", ispunct('1'));
  printf("1 isspace or not      : %d\n", isspace('1'));
  printf("1 isupper or not      : %d\n", isupper('1'));
  printf("1 isxdigit or not     : %d\n", isxdigit('1'));
  printf("1 isspace or not      : %d\n", isspace('1'));
  printf("\\n isspace or not    : %d\n", isspace('\n'));
  printf("\\t isspace or not    : %d\n", isspace('\t'));
  printf("[SPC] isspace or not  : %d\n", isspace(' '));
  printf("A tolower is          : %c\n", tolower('A'));
  printf("a toupper is          : %c\n", toupper('a'));

  return 1;
}