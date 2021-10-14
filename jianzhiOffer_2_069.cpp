#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;

class Solution {
public:
    int peakIndexInMountainArray(vector<int> &arr) {
        int n = arr.size();
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l + 1) / 2;
            if (arr[mid - 1] < arr[mid]) l = mid;
            else r = mid - 1;
        }
        return l;
    }
};

int main() {
    Solution s{};
    vector<int> arr{0, 2, 1, 0};
    cout << s.peakIndexInMountainArray(arr) << endl;
}
