class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        // Initialize dummy node and current pointer
        ListNode *dummy = new ListNode();
        ListNode *current = dummy;
        int carry = 0;

        // Traverse both linked lists
        while (l1 != nullptr || l2 != nullptr || carry != 0)
        {
            // Get the values from the current nodes
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;

            // Calculate the sum and update carry
            int total = val1 + val2 + carry;
            carry = total / 10;
            int new_val = total % 10;

            // Create a new node with the sum and move the pointer
            current->next = new ListNode(new_val);
            current = current->next;

            // Move to the next nodes in the input lists
            if (l1 != nullptr)
                l1 = l1->next;
            if (l2 != nullptr)
                l2 = l2->next;
        }

        // Return the result linked list
        return dummy->next;
    }
};
