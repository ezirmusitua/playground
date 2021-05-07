#include <stdio.h>
#define ROWS 4
#define COLS 4

void sum_rows(int ar[][COLS], int rows)
{
  for (int r = 0, total = 0; r < rows; r += 1, total = 0)
  {
    for (int c = 0; c < COLS; c += 1)
    {
      total += ar[r][c];
    }
    printf("row %d: sum: %d\n", r, total);
  }
}

void sum_cols(int ar[][COLS], int rows)
{
  for (int c = 0, total = 0; c < COLS; c += 1, total = 0)
  {
    for (int r = 0; r < rows; r += 1)
    {
      total += ar[r][c];
    }
    printf("col %d: sum: %d\n", c, total);
  }
}

int sum2d(int (*ar)[COLS], int rows)
{
  int total = 0;
  for (int r = 0; r < rows; r += 1)
  {
    for (int c = 0; c < COLS; c += 1)
    {
      total += ar[r][c];
    }
  }
  printf("sum: %d\n", total);
  return total;
}

int debug(int ar[ROWS][COLS])
{
  int total = 0;
  for (int r = 0; r < ROWS; r += 1)
  {
    for (int c = 0; c < COLS; c += 1)
    {
      total += ar[r][c];
    }
  }
  printf("sum: %d\n", total);

  return total;
}

int main()
{
  int junk[ROWS][COLS] = {
      {2, 4, 6, 8},
      {3, 5, 7, 9},
      {4, 6, 8, 10},
      {5, 7, 9, 11},
  };

  sum_rows(junk, ROWS);
  sum_cols(junk, ROWS);
  printf("Sum of all elements = %d\n", sum2d(junk, ROWS));
  printf("Sum of all elements = %d\n", debug(junk));

  return 1;
}