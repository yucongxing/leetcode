#include <vector>
using namespace std;
class Solution {
public:
    int superPow(int a, vector<int>& b) {
        int re[1337] = {0};
        re[1] = 1;
        for (int i = 2; i < 1337; ++i) {
            int ret = 1;
            for (int j = 0; j < 10; ++j) {
                ret = (ret * i) % 1337;
            }
            re[i] = ret;
            //cout << ret << endl;
        }
        int n = b.size();
        vector<int> ans(n, 0);
        a %= 1337;

        for (int i = 0; i < n; ++i) {
            int t = a;
            int cnt = n - 1 - i;
            while (cnt--) {
                t = re[t];
            }
            int ret = 1;
            for (int j=0; j < b[i]; ++j) {
                ret = (ret * t) % 1337;
            }
            ans[i] = ret;
        }
        int result = 1;
        for (int i =0; i < n; ++i){
            result = (result * ans[i]) % 1337;
        }
        return result;
    }
};
