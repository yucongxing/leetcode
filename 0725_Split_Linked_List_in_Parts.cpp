#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0, head);
        int len = 0;
        ListNode* p = dummy;
        while (p->next) {
            p = p->next;
            len++;
        }
        vector<ListNode*> ans(k, nullptr);
        int avg = len / k, extra = len % k;
        p = dummy;
        int cnt = 0, partscnt = 0;
        while (p->next) {
            p = p->next;
            cnt++;
            if ((partscnt < extra && cnt == avg + 1) || (partscnt >= extra && cnt == avg)) {
                ans[partscnt] = dummy->next;
                dummy->next = p->next;
                p->next = nullptr;
                p = dummy;
                cnt = 0;
                partscnt++;
            }
        }
        delete dummy;
        return ans;
    }
};

int main() {
    Solution s;
    return 0;
}
