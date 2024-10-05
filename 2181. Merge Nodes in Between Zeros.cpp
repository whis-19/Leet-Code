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
    ListNode *mergeNodes(ListNode *head)
    {
        ListNode *temp = new ListNode(0); // A temp node to simplify edge cases
        ListNode *current = temp;         // Pointer to construct the new list
        int temp_sum = 0;                 // Variable to sum the values between zeros

        // Skip the initial zero
        head = head->next;

        while (head)
        {
            if (head->val == 0)
            {
                // Encounter a zero, meaning end of a segment
                current->next = new ListNode(temp_sum); // Create a new node with the sum
                current = current->next;                // Move to the new node
                temp_sum = 0;                           // Reset the sum for the next segment
            }
            else
            {
                // Accumulate the sum
                temp_sum += head->val;
            }
            head = head->next; // Move to the next node
        }

        return temp->next; // Return the new list, skipping the temp node
    }
};