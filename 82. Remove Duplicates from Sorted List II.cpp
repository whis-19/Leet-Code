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
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (!head)
        {
            return nullptr;
        }

        // Dummy node
        ListNode *dummy = new ListNode(0, head);
        ListNode *prev = dummy; // The last node before the sequence of duplicates
        ListNode *current = head;

        while (current)
        {
            // If it's the beginning of duplicates sequence
            // Skip all duplicates
            if (current->next && current->val == current->next->val)
            {
                // Move till the end of duplicates sequence
                while (current->next && current->val == current->next->val)
                {
                    current = current->next;
                }
                // Skip all duplicates
                prev->next = current->next;
            }
            else
            {
                // No duplicates, move prev pointer
                prev = prev->next;
            }
            // Move current pointer
            current = current->next;
        }

        return dummy->next;
    }
};
