#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

class Solution {
public:
    string getHint(string secret, string guess) {
        int res[10] = {0}, reg[10] = {0};
        int x{0}, y{0};
        for (int i = 0; i < secret.length(); ++i) {
            if (guess[i] == secret[i]) {
                ++x;
            }else {
                res[secret[i] - '0']++;
                reg[guess[i] - '0']++;
            }
        }
        for (int i = 0; i < 10; ++i) {
            y += min(res[i], reg[i]);
        }
        return to_string(x) + "A" + to_string(y) + "B";
    }
};

int main() {
    Solution s;
    string secret{"1123"}, guess{"0111"};
    cout << s.getHint(secret, guess) << endl;
    return 0;
}
