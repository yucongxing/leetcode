#include <vector>
#include <iostream>

class Node {
public:
    int val{0};
    std::vector<Node*> children{};

    Node() {}

    Node(int _val) : val(_val) {}

    Node(int _val, std::vector<Node*> _children) : val(_val), children(_children) {}
};

class Solution {
public:
    int maxDepth(Node *root) {
        if (!root) return 0;
        int maxD{0};
        for (auto &&node : root->children) {
            maxD = std::max(maxD, maxDepth(node));
        }
        return maxD + 1;
    }
};

