#include <string>
#include <iostream>
#include <vector>
class MapSum {
public:
    MapSum *next[26];
    int val{0};
    bool isEnd = false;
    MapSum() : val(0), isEnd(false) {
        for (int i = 0; i < 26; ++i) {
            next[i] = nullptr;
        }
    }

    void insert(std::string key, int val) {
        MapSum *p = this;
        std::vector<MapSum*> path{};
        for (int i = 0; i < key.length(); ++i) {
            int index = key[i] - 'a';
            if (p->next[index] == nullptr) {
                p->next[index] = new MapSum();
            }
            p = p->next[index];
            path.push_back(p);
        }
        if (!p->isEnd) {
            for (auto && node : path) {
                node->val += val;
            }
            p->isEnd = true;
        }else {
            int preval = p->val;
            for (int i = 0; i < 26; ++i) {
                if (p->next[i]) {
                    preval -= p->next[i]->val;
                }
            }
            for (auto && node : path) {
                node->val = node->val - preval + val;
            }
        }
    }

    int sum(std::string prefix) {
        MapSum *p = this;
        for (auto && ch : prefix) {
            if (p->next[ch - 'a'] == nullptr) {
                return 0;
            }
            p = p->next[ch - 'a'];
        }
        return p->val;
    }

};

int main() {
    MapSum ms;
    ms.insert("appled", 2);
    std::cout << ms.sum("a") << std::endl;
    ms.insert("apple", 3);
    std::cout << ms.sum("a") << std::endl;
    ms.insert("apple", 2);
    std::cout << ms.sum("apple") << std::endl;
    return 0;
}
