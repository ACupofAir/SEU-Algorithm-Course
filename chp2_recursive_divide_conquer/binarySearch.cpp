#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;

int binarySearch(int *arr, int left, int right, int value) {
  int med = (left + right) / 2;
  if (left == right)
    return -1;
  if (arr[med] == value)
    return med;
  else if (arr[med] < value)
    return binarySearch(arr, med + 1, right, value);
  else
    return binarySearch(arr, left, med - 1, value);
}

int main(void) {
  int arr[100];
  for (int i = 0; i < 100; i++)
    arr[i] = rand() % 100;
  sort(arr, arr + sizeof(arr) / sizeof(arr[0]));
  cout << binarySearch(arr, 0, 99, 21); 
  return 0;
}
