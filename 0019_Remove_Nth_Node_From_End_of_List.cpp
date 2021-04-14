struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int cnt=0;
        ListNode *p=head,*q=head,*pre=nullptr;
        while(cnt<n && p){
            p=p->next;
            cnt++;
        }
        if(cnt<n) return head;
        while(p){
            p=p->next;
            pre=q;
            q=q->next;
        }
        if(q==head){
            head=q->next;
            delete(q);
        }else{
            pre->next=q->next;
            delete(q);
        }
        return head;
    }
};