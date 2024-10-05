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
    ListNode *rotateRight(ListNode *head, int k)
    {
        if (!head || !head->next || k == 0)
            return head;

        // Step 1: Determine the length of the list
        ListNode *current = head;
        int length = 1;
        while (current->next)
        {
            current = current->next;
            length++;
        }

        // Step 2: Make the list circular
        current->next = head;

        // Step 3: Find the new head and tail
        k = k % length; // In case k is larger than the length
        int stepsToNewHead = length - k;
        ListNode *newTail = current;
        while (stepsToNewHead--)
        {
            newTail = newTail->next;
        }
        ListNode *newHead = newTail->next;
        newTail->next = nullptr;

        return newHead;
    }
};