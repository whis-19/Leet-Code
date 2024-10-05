class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *first = dummy;
        ListNode *second = dummy;

        for (int i = 1; i <= n + 1; ++i)
        {
            first = first->next;
        }

        while (first != nullptr)
        {
            first = first->next;
            second = second->next;
        }

        ListNode *nodeToRemove = second->next;
        second->next = second->next->next;
        delete nodeToRemove;

        ListNode *newHead = dummy->next;
        delete dummy;
        return newHead;
    }
};
