#include <stdio.h>
#define MSG "I'm special"

int main() {
  char ar[] = MSG;
  char *pt = MSG;
  const char *cpt = MSG;

  printf("address of \"I'm special\": %p \n", "I'm special");
  printf("           address of ar: %p \n", ar);
  printf("           address of pt: %p \n", pt);
  printf("          address of cpt: %p \n", cpt);
  printf("          address of MSG: %p \n", MSG);
  printf("address of \"I'm special\": %p \n", "I'm special");

  const char *p1 = "Klingon";
  printf("p1[0]: %c\n", p1[0]);
  // p1[0] = 'c';
  printf("Klingon");
  printf(": Beware the %ss!\n", "Klingon");

  return 1;
}