#include <stdio.h>

const int S_PER_M = 60;
const int S_PER_H = 3600;
const double M_PER_K = 0.62317;

int main() {
  printf("This program converts your time for a metric race\n");
  printf("to a time for running a mile and to your average\n");
  printf("speed in miles per hour.\n");
  printf("Please enter, in kilometers, the distance run.\n");
  double distk;
  scanf("%lf", &distk); // %lf for type double
  printf("Next enter the time in minutes and seconds.\n");
  printf("Begin by entering the minutes.\n");
  int min;
  scanf("%d", &min);
  printf("Now enter the seconds.\n");
  int sec;
  scanf("%d", &sec);
  // converts time to pure seconds
  int time = S_PER_M * min + sec;
  // converts kilometers to miles
  double distm = M_PER_K * distk;
  // miles per sec x sec per hour = mph
  double rate = distm / time * S_PER_H;
  // time/distance = time per mile
  double mtime = (double)time / distm;
  int mmin = (int)mtime / S_PER_M; // find whole minutes
  int msec = (int)mtime % S_PER_M; // find remaining seconds
  printf("You ran %1.2f km (%1.2f miles) in %d min, %d sec.\n", distk, distm, min, sec);
  printf("That pace corresponds to running a mile in %d min, ", mmin);
  printf("%d sec.\nYour average speed was %1.2f mph.\n", msec, rate);
  return 1;
}