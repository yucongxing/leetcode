#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

class Solution {
public:
    int compareVersion(string version1, string version2) {
        auto i = version1.begin();
        auto j = version2.begin();
        int val1 = 0, val2 = 0;
        while (i != version1.end() && j != version2.end()) {
            // cout << *i << " " << *j << endl;
            if (*i == *j && *i == '.') {
                if (val1 > val2 ) {
                    return 1;
                }else if (val1 < val2) {
                    return -1;
                }
                val1 = val2 = 0;
                i++;
                j++;
            }else if (*i == '.') {
                val2 = val2 * 10 + *j - '0';
                j++;
            }else if (*j == '.') {
                val1 = val1 * 10 + *i - '0';
                i++;
            }else{
                val1 = val1 * 10 + *i - '0';
                val2 = val2 * 10 + *j - '0';
                i++;
                j++;
            }
        }
        while (i != version1.end()) {
            if (*i == '.') {
                if (val1 > val2) {
                    return 1;
                }else if (val1 < val2) {
                    return -1;
                }
                val1 = val2 = 0;
                i++;
            }else {
                val1 = val1 * 10 + *i - '0';
                i++;
            }
        }
        while (j != version2.end()) {
            if (*j == '.') {
                if (val1 > val2) {
                    return 1;
                }else if (val1 < val2) {
                    return -1;
                }
                val1 = val2 = 0;
                j++;
            }else {
                val2 = val2 * 10 + *j - '0';
                j++;
            }
        }
        return val1 > val2 ? 1 : (val1 == val2 ? 0 : -1);
    }
};

int main() {
    Solution s;
    cout << s.compareVersion("7.5.2.4", "7.5.3") <<endl; // -1
    cout << s.compareVersion("1.0.1", "1") <<endl; // 1
    cout << s.compareVersion("1.01", "1.001") <<endl; // 0
    cout << s.compareVersion("0.1", "1.1") <<endl; // -1
    cout << s.compareVersion("1.0", "1.0.0") <<endl; // 0
}
