#include <bits/stdc++.h>
using namespace std;
struct TreeNode{
    int val;
    TreeNode *left,*right;
};
class Solution {
public:
    TreeNode* invertTree(TreeNode* root){
        if(!root) return root;
        TreeNode *left=invertTree(root->left);
        TreeNode *right=invertTree(root->right);
        root->left=right;
        root->right=left;
        return root;
    }
};
int main(){
    
    return 0;
}
