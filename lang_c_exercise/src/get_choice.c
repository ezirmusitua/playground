#include <stdio.h>
#include <inttypes.h>

char get_first()
{
  uint32_t ch = getchar();
  while (getchar() != '\n')
  {
    continue;
  }
  return ch;
}

uint32_t get_choice()
{
  uint32_t ch = get_first();
  while ((ch < 'a' || ch > 'c') && ch != 'q')
  {
    printf("Please respond with a, b, c, d or press q to exit. \n");
    ch = getchar();
  }

  return ch;
}

int main()
{
  printf("Enter the letter of your choice\n");
  printf("a. advice          b. bell\n");
  printf("c. count           d. quit\n");
  uint32_t choice = get_choice();
  if (choice == 'q') {
    printf("See you next time");
    return 0;
  }
  printf("Your choice is %c", choice);
  return 1;
}