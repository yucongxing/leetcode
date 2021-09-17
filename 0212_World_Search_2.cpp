#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
typedef long long ll;

struct TrieNode {
    TrieNode* next[26];
    string word = "";
    TrieNode() {
        for (int i = 0; i < 26; i++) {
            next[i] = nullptr;
        }
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (auto& word : words) {
            TrieNode* p = root;
            for (int i = 0; i < word.length(); i++) {
                if (p->next[word[i] - 'a'] == nullptr) {
                    p->next[word[i] - 'a'] = new TrieNode();
                }
                p = p->next[word[i] - 'a'];
            }
            p->word = word;
        }
        vector<string> res;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(root, board, i, j, res);
            }
        }
        return res;
    }

    void dfs(TrieNode* root, vector<vector<char>>& board, int i, int j, vector<string> &res) {
        if(i < 0 || j < 0 || i >= board.size() || j >= board[0].size()) return;
        char ch = board[i][j];
        if (ch == '*' || root->next[ch - 'a'] == nullptr) return;
        root = root->next[ch - 'a'];
        if (root->word != "") {
            res.push_back(root->word);
            root->word = "";
        }
        board[i][j] = '*';
        dfs(root, board, i - 1, j, res);
        dfs(root, board, i, j + 1, res);
        dfs(root, board, i + 1, j, res);
        dfs(root, board, i, j - 1, res);
        board[i][j] = ch;
    }
};

int main() {
    Solution s;
    vector<vector<char>> board{{'o','a','a','n'}, {'e', 't', 'a', 'e'}, {'i', 'h', 'k', 'r'}, {'i', 'f', 'l', 'v'}};
    vector<string> words{"oath", "pea", "eat", "rain"};
    vector<string> ans = s.findWords(board, words);
    for (auto w : ans) {
        cout << w << endl;
    }
    return 0;
}
