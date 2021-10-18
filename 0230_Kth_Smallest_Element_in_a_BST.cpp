#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;
typedef long long ll;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {};
    TreeNode(int x, TreeNode* left, TreeNode *right): val(x), left(left), right(right) {}
};

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s{};
        TreeNode *p = root;
        int cnt = 0;
        while (p != nullptr) {
            s.push(p);
            p = p->left;
        }
        while (!s.empty()) {
            p = s.top();
            cnt++;
            if (cnt == k) return p->val;
            s.pop();
            if (p->right != nullptr) {
                p = p->right;
                while (p != nullptr) {
                    s.push(p);
                    p = p->left;
                }
            }
        }
        return 0;
    }
};

int main() {
    Solution s;
    return 0;
}
