#include <iostream>
using namespace std;

int q(int n, int m) {
  if (n < 1 || m < 1)
    return 0;
  else if (n == 1 || m == 1) {
    return 1;
  } else if (n < m) {
    return q(n, n);
  } else if (n == m) {
    return q(n, m - 1) + 1;
  } else {
    return q(n, m - 1) + q(n - m, m);
  }
}

int main(void) {
  cout << "Input a number:\n";
  int n;
  cin >> n;
  cout << "The divide of the number has " << q(n,n) <<" methods.";
  return 0;
}
