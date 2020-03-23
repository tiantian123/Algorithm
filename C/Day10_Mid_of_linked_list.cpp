#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* middleNode1(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != NULL && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    ListNode* middleNode2(ListNode* head) {
        int cnt = 0;
        ListNode* pos = head;
        while (pos) {
            cnt ++;
            pos = pos->next;
        }
        int k = 0;
        pos = head;
        while (k < cnt / 2) {
            k ++;
            pos = pos->next;
        }
        return pos;
        
    }
};