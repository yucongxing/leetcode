#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
using namespace std;
typedef long long ll;

class WordDictionary {
public:
    WordDictionary() {
        for (int i = 0; i< N; i++) {
            next[i] = nullptr;
        }
    }

    void addWord(string word) {
        int n = word.length();
        WordDictionary* p = this;
        for (int i = 0; i < n; i++) {
            int nextIndex = word[i] - 'a';
            if (p->next[nextIndex] == nullptr) {
                WordDictionary* t = new WordDictionary();
                p->next[nextIndex] = t;
            }
            p = p->next[nextIndex];
        }
        p->end = true;
    }

    bool search(string word) {
        int n = word.length();
        WordDictionary* p = this;
        function<bool(WordDictionary*, int)> dfs = [&] (WordDictionary *root, int i) {
            if (root == nullptr) return false;

            if (i == n) return root->end;

            if (word[i] == '.') {
                for (int j = 0; j < 26; j++) {
                    if (dfs(root->next[j], i + 1)) return true;
                }
                return false;
            }else {
                return dfs(root->next[word[i] - 'a'], i + 1);
            }
        };
        return dfs(p, 0);
    }
private:
    static constexpr int N = 26;
    WordDictionary* next[N];
    bool end{false};
};

int main() {
    WordDictionary *wd = new WordDictionary();
    wd->addWord("bad");
    wd->addWord("dad");
    wd->addWord("mad");
    cout << wd->search("pad") << endl;
    cout << wd->search("bad") << endl;
    cout << wd->search(".ad") << endl;
    cout << wd->search("b..") << endl;
    return 0;
}
// function<> 的使用会导致效率降低，关键词 內联（inline）
