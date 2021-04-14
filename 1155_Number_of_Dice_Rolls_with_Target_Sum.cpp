#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int numRollsToTarget(int d, int f, int target) {
        if(target < d || target / d > f) return 0;
        else{
            int n = target - d;
            long long ans=1,mod=1000000000 + 7;
            for(int i=0;i<n;i++){
                ans = (ans*d)%mod;
            }
            return (int)ans;
        }
    }
};
int main(){
    Solution s;
    int ans = s.numRollsToTarget(30,30,500);
    printf("%d",ans);
    return 0;
}
