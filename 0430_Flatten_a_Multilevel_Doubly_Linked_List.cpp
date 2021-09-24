#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
public:
    void dfs(Node *root) {
        if (root == nullptr) return;
        if (root->child) {
            dfs(root->child);
            Node* p = root->child;
            while(p->next){
                p = p->next;
            }
            root->next->prev = p;
            p->next = root->next;
            root->next = root->child;
            root->child = nullptr;
            dfs(p->next);
        }else dfs(root->next);
    }
    Node* flatten(Node* head) {
        dfs(head);
        return head;
    }
};

int main() {
    Solution s;

    return 0;
}
