#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
  int integerReplacement(int n) {
      ll x = (ll)n;
      int cnt = 0;
      while (x != 1) {
          if (x & 1) {
              if (x & 2 && x != 3) {
                  x += 1;
              }else {
                  x -= 1;
              }
          } else {
              x /= 2;
          }
          ++cnt;
      }
      return cnt;
  }
};

int main() {
    Solution s;
    cout << s.integerReplacement(8) << endl;
    cout << s.integerReplacement(7) << endl;
    cout << s.integerReplacement(4) << endl;
    return 0;
}
