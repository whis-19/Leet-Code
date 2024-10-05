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
    ListNode *partition(ListNode *head, int x)
    {
        // Create two dummy nodes to start the less and greater lists
        ListNode less_head(0);
        ListNode greater_head(0);

        // Pointers to the current node in less and greater lists
        ListNode *less = &less_head;
        ListNode *greater = &greater_head;

        // Traverse the original list
        while (head != nullptr)
        {
            if (head->val < x)
            {
                // Insert node into the less list
                less->next = head;
                less = less->next;
            }
            else
            {
                // Insert node into the greater list
                greater->next = head;
                greater = greater->next;
            }
            head = head->next;
        }

        // Terminate the greater list
        greater->next = nullptr;

        // Connect the less list with the greater list
        less->next = greater_head.next;

        // Return the head of the new list
        return less_head.next;
    }
};