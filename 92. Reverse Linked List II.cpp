/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        if (!head || left == right)
            return head;

        ListNode temp(0);
        temp.next = head;
        ListNode *prev = &temp;

        // Move `prev` to the node before the `left` position
        for (int i = 1; i < left; ++i)
        {
            prev = prev->next;
        }

        ListNode *start = prev->next;
        ListNode *then = start->next;

        // Reverse the nodes from `left` to `right`
        for (int i = 0; i < right - left; ++i)
        {
            start->next = then->next;
            then->next = prev->next;
            prev->next = then;
            then = start->next;
        }

        return temp.next;
    }
};