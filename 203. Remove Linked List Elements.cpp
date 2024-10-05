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
    ListNode *removeElements(ListNode *head, int val)
    {
        // Create a dummy node that points to the head
        ListNode *dummy = new ListNode(0, head);
        ListNode *prev = dummy;
        ListNode *current = head;

        while (current != nullptr)
        {
            if (current->val == val)
            {
                // Remove current node by skipping it
                prev->next = current->next;
            }
            else
            {
                // Move prev pointer forward
                prev = current;
            }
            // Move current pointer forward
            current = current->next;
        }

        // The new head is the next node of dummy
        ListNode *new_head = dummy->next;
        delete dummy; // Clean up the dummy node
        return new_head;
    }
};
