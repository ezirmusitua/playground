#include <stdio.h>
#define MAX_DATA_SIZE 100

int read_data(int data[MAX_DATA_SIZE]) {
  int counter = 0;
  int value;
  printf("Enter integer for summing up, enter 999 to end input\n");
  do {
    printf("Enter: ");
    scanf("%d", &value);
    data[counter] = value;
    counter += 1;
  } while(value != 999 && counter != MAX_DATA_SIZE);
  data[counter - 1] = 0;
  return counter;
}

int sum_with_while(int data[MAX_DATA_SIZE], int size) {
  int index = 0;
  int sum = 0;
  while(index < size) {
    sum += data[index];
    index += 1;
  }
  return sum;
}

int sum_with_for(int data[MAX_DATA_SIZE], int size) {
  int sum = 0;
  for (int i = 0; i < size; i += 1, sum += data[i]);
  return sum;
}

int sum_with_dowhile(int data[MAX_DATA_SIZE], int size) {
  int i = 0;
  int sum = 0;
  do {
    sum += data[i];
    i += 1;
  } while(i < size);
  return sum;
}

int main() {
  int data[MAX_DATA_SIZE];
  int size = read_data(data);
  printf("Do sum up with while loop   : %d\n", sum_with_while(data, size));
  printf("Do sum up with for loop     : %d\n", sum_with_for(data, size));
  printf("Do sum up with dowhile loop : %d\n", sum_with_dowhile(data, size));
  return 1;
}