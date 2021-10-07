#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int countSegments(string s) {
        int n = s.length();
        bool flag = false;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != ' ') {
                flag = true;
            }else {
                if (flag) ans++;
                flag = false;
            }
            if (flag && i == n - 1) ans++;
        }
        return ans;
    }
};

int main() {
    Solution s;
    string str = "a";
    cout << s.countSegments(str) << endl;
    return 0;
}
