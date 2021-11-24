#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Solution {
public:
    // zero one two three four five six seven eight nine
    // z : zero u : four x: six g: eight w: two
    // r: three s: seven o:one
    // v five n: nine
    // e: 0 1 3 5 7 8 9
    // f: 4 5
    // g: 8
    // h: 3 8
    // i: 5 6 8 9
    // n: 1 7 9
    // o: 0 1 2 4
    // r: 0 3 4
    // s: 6 7
    // t: 2 3 8
    // u: 4
    // v: 5 7
    // w: 2
    // x: 6
    // z: 0
    string originalDigits(string s) {
        int re[26] = {0};
        for (auto && ch : s) {
            re[ch - 'a']++;
        }
        for (int i = 0; i < 26; ++i) {
            if (re[i] > 0) {
                cout << char(i + 'a') << endl;
            }
        }
        string ans{};
        ans += string(re['z' - 'a'], '0');
        ans += string(re['o' - 'a'] - re['w' - 'a'] - re['z' - 'a'] - re['u' - 'a'], '1');
        ans += string(re['w' - 'a'], '2');
        ans += string(re['r' - 'a'] - re['z' - 'a'] - re['u' - 'a'], '3');
        ans += string(re['u' - 'a'], '4');
        ans += string(re['f' - 'a'] - re['u' - 'a'], '5');
        ans += string(re['x' - 'a'], '6');
        ans += string(re['s' - 'a'] - re['x' - 'a'], '7');
        ans += string(re['g' - 'a'], '8');
        ans += string(re['i' - 'a'] - re['x' - 'a'] - re['g' - 'a'] - (re['f' - 'a'] - re['u' - 'a']), '9');
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.originalDigits("owoztneoer") << endl;
    return 0;
}
