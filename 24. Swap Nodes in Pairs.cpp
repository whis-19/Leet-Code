class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *prev = dummy;

        while (prev->next && prev->next->next)
        {
            ListNode *first = prev->next;
            ListNode *second = prev->next->next;

            // Swapping nodes
            prev->next = second;
            first->next = second->next;
            second->next = first;

            // Move prev to the next pair
            prev = first;
        }

        return dummy->next;
    }
};