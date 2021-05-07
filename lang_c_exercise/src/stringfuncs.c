#include <stdio.h>
#include <string.h>
#define SIZE 80
#define LISTSIZE 6
#define LIM 5

char *s_gets(char *st, int n)
{
  char *ret_val;
  int i = 0;

  ret_val = fgets(st, n, stdin);
  if (ret_val)
  {
    while (st[i] != '\n' && st[i] != '\0')
      i++;
    if (st[i] == '\n')
      st[i] = '\0';
    else // must have words[i] == '\0'
      while (getchar() != '\n')
        continue;
  }
  return ret_val;
}

void fit(char *string, unsigned int size)
{
  if (strlen(string) > size)
  {
    string[size] = '\0';
  }
}

int main(void)
{
  char mesg[] = "Things should be as simple as possible,"
                " but not simpler.";

  puts(mesg);
  fit(mesg, 38);
  puts(mesg);
  puts("Let's look at some more of the string.");
  puts(mesg + 39);

  char flower1[SIZE];
  char flower2[SIZE];
  char addon[] = "s smell like old shoes.";

  puts("What is your favorite flower?");
  if (s_gets(flower1, SIZE))
  {
    strcat(flower1, addon);
    strncat(flower2, addon, 5);
    puts("strcpy");
    puts(flower1);
    puts("strncpy");
    puts(flower2);
    puts(addon);
  }
  else
  {
    puts("End of file encountered!");
  }

  printf("strcmp(\"A\", \"A\") is ");
  printf("%d\n", strcmp("A", "A"));
  printf("strcmp(\"A\", \"B\") is ");
  printf("%d\n", strcmp("A", "B"));
  printf("strcmp(\"B\", \"A\") is ");
  printf("%d\n", strcmp("B", "A"));
  printf("strcmp(\"C\", \"A\") is ");
  printf("%d\n", strcmp("C", "A"));
  printf("strcmp(\"Z\", \"a\") is ");
  printf("%d\n", strcmp("Z", "a"));
  printf("strcmp(\"apples\", \"apple\") is ");
  printf("%d\n", strcmp("apples", "apple"));

  const char *list[LISTSIZE] =
      {
          "astronomy", "astounding",
          "astrophysics", "ostracize",
          "asterism", "astrophobia"};
  int count = 0;
  int i;

  for (i = 0; i < LISTSIZE; i++)
    if (strncmp(list[i], "astro", 5) == 0)
    {
      printf("Found: %s\n", list[i]);
      count++;
    }
  printf("The list contained %d words beginning"
         " with astro.\n",
         count);

  char qwords[LIM][SIZE];
  char temp[SIZE];
  i = 0;

  printf("Enter %d words beginning with q:\n", LIM);
  while (i < LIM && s_gets(temp, SIZE))
  {
    if (temp[0] != 'q')
      printf("%s doesn't begin with q!\n", temp);
    else
    {
      strcpy(qwords[i], temp);
      i++;
    }
  }
  puts("Here are the words accepted:");
  for (int k = 0; k < LIM; k++)
    puts(qwords[k]);
  puts("bye");

  return 0;
}
