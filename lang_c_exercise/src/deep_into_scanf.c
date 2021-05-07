#include <assert.h>
#include <stdio.h>
#define MAX_NAME_LEN 20

void deep_int_scanf() {
  int age;
  char name[MAX_NAME_LEN];
  char confirm = 'n';

  printf("Please input your name and age, seperate by [SPC]\n");
  scanf("%s %d\n", name, &age);
  printf("Your name is %s, and your age is %d, do you confirm?\n", name, age);
  scanf("%c", &confirm);
  // assert(confirm[0] == 'y');

  return;
}

int main() {
  deep_int_scanf();
  return 1;
}