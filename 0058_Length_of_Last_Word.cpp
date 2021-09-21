#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.length() - 1;
        while (s[i] == ' ') {
            i--;
        }
        int ans = 0;
        while (s[i] != ' ' && i >= 0) {
            i--;
            ans++;
        }
        return ans;
    }
};

int main() {
    Solution s;
    string str = "a";
    cout << s.lengthOfLastWord(str) << endl;
    return 0;
}
