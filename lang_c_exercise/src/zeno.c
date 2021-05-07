#include <stdio.h>

void zeno() {
  int t_ct;
  int limit;
  double time;
  double power_of_2;

  printf("Enter the number of terms you want: ");
  scanf("%d", &limit);

  for (time = 0.0f, power_of_2 = 1.0f, t_ct = 1; t_ct <= limit; t_ct += 1, power_of_2 *= 2.0) {
    time += 1.0 / power_of_2;
    printf("time = %f when terms = %d.\n", time, t_ct);
  }
}

int main() {
  zeno();
  return 1;
}