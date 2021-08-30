#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <random>
#include <iterator>
using namespace std;

class Solution{
private:
    mt19937 gen;
    uniform_int_distribution<int> dis;
    vector<int> presum;

public:
    Solution(vector<int>& w): gen(random_device{}()), dis(1, accumulate(w.begin(), w.end(), 0)) {
     partial_sum(w.begin(), w.end(), back_inserter(presum));
    }

    int pickIndex() {
        int x = dis(gen);
        return lower_bound(presum.begin(), presum.end(), x) - presum.begin();
    }
};

int main() {
    vector<int> w = {1, 2, 5, 8};
    Solution s(w);
    int cnt = 100;
    while (cnt) {
        cnt--;
        cout << s.pickIndex() << endl;
    }
}
