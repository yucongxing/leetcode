#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
typedef long long ll;

class Solution {
public:
    map<vector<int>, int> memo{};
    int shoppingOffers(vector<int> &price, vector<vector<int>> &special, vector<int>& needs) {
        int n = price.size();
        vector<vector<int>> filterSpecial;
        for (auto&& sp : special) {
            int totalCount = 0, totalPrice = 0;
            for (int i = 0; i < n; ++i) {
                totalCount += sp[i];
                totalPrice += sp[i] * price[i];
            }
            if (totalCount > 0 && totalPrice > sp[n]) {
                filterSpecial.emplace_back(sp);
            }
        }


        return dfs(price, needs, filterSpecial, n);
    }
    int dfs(vector<int> &price, vector<int> curNeeds, vector<vector<int>> &filterSpecial, int n) {
        if (!memo.count(curNeeds)) {
            int minPrice{0};
            for (int i = 0; i < n; ++i) {
                minPrice += curNeeds[i] * price[i];
            }
            for (auto&& curSpecial : filterSpecial) {
                int specialPrice = curSpecial[n];
                vector<int> nextNeeds{};
                for (int i = 0; i < n; ++i) {
                    if (curSpecial[i] > curNeeds[i]) {
                        break;
                    }
                    nextNeeds.emplace_back(curNeeds[i] - curSpecial[i]);
                }
                if (nextNeeds.size() == n) {
                    minPrice = min(minPrice, dfs(price, nextNeeds, filterSpecial, n) + specialPrice);
                }
            }
            memo[curNeeds] = minPrice;
        }
        return memo[curNeeds];
    }
};

int main() {
    Solution s;
    vector<int> price{2, 5};
    vector<vector<int>> special{{3, 0, 5}, {1, 2, 10}};
    vector<int> needs{3, 2};
    cout << s.shoppingOffers(price, special, needs) << endl;
    return 0;
}
