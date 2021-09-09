#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string blank(int n) {
        return string(n, ' ');
    }

    string join(vector<string> &words, int left, int right, string sep) {
        string ret = words[left];
        for (int i = left + 1; i< right; ++i) {
            ret += sep + words[i];
        }
        return ret;
    }

    vector<string> fullJustify(vector<string>& words, int maxWidth) {
         vector<string> ans;
         int right = 0, n = words.size();
         while (true) {
             int left = right;
             int sum_len = 0;
             while (right < n && int(sum_len + words[right].length() + right - left) <= maxWidth) {
                 sum_len += words[right++].length();
             }
             if (right == n) {
                 string s = join(words, left, n, " ");
                 ans.emplace_back(s + blank(maxWidth - s.length()));
                 return ans;
             }

             int num_words = right - left;
             int num_spaces = maxWidth - sum_len;

             if (num_words == 1) {
                 ans.emplace_back(words[left] + blank(num_spaces));
                 continue;
             }

             int avg_spaces = num_spaces / (num_words - 1);
             int extra_spaces = num_spaces % (num_words - 1);
             string s1 = join(words, left, left + extra_spaces + 1, blank(avg_spaces + 1));
             string s2 = join(words, left + extra_spaces + 1, right, blank(avg_spaces));
             ans.emplace_back(s1 + blank(avg_spaces) + s2);
         }
    }
};

int main() {
    Solution s;
    vector<string> words{"This", "is", "an", "example", "of", "text", "justification."};
    int maxWidth = 16;
    vector<string> justified =  s.fullJustify(words, maxWidth);
    for (auto w : justified) {
        cout << w << endl;
    }
}
