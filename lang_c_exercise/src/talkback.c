#include <stdio.h>
#include <string.h>
#define DENSITY 62.4
#define MAX_NAME_LEN 5

void talkback(void) {
  float weight;
  char name[MAX_NAME_LEN];

  printf("Hi! What's your first name?\n");
  scanf("%s", name);
  int size = sizeof(name);
  int letter_count = strlen(name);
  printf("%s, What's your weight in pounds?\n", name);
  scanf("%f", &weight);
  float volume = weight / DENSITY;

  printf("Well, %s, your volume is %2.2f cubic feet.\n", name, volume);
  printf("Also, your first name has %d letters, \n", letter_count);
  printf("and we have %d bytes to store it. \n", size);

  return;
}

int main() {
  talkback();
  return 0;
}