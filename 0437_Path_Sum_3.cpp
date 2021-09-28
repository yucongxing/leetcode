#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int cnt = 0;
    int ans = 0;
    void dfs(TreeNode* root, int targetSum, int curSum) {
        if (root == nullptr) return;
        curSum += root->val;
        if (curSum == targetSum) cnt++;
        dfs(root->left, targetSum, curSum);
        dfs(root->right, targetSum, curSum);
        curSum -= root->val;
    }

    void ddfs(TreeNode* root, int targetSum) {
        if (root == nullptr) return;
        cnt = 0;
        dfs(root, targetSum, 0);
        ans += cnt;
        ddfs(root->left, targetSum);
        ddfs(root->right, targetSum);
    }

    int pathSum(TreeNode* root, int targetSum) {
        ddfs(root, targetSum);
        return ans;
    }
};

int main() {
    Solution s;
    return 0;
}
