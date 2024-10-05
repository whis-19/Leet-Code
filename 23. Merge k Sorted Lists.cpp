class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode dummy(0);
        ListNode *current = &dummy;

        while (l1 && l2)
        {
            if (l1->val < l2->val)
            {
                current->next = l1;
                l1 = l1->next;
            }
            else
            {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }

        if (l1)
        {
            current->next = l1;
        }
        else
        {
            current->next = l2;
        }

        return dummy.next;
    }

    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.empty())
            return nullptr;

        int n = lists.size();

        // Merge lists iteratively
        while (n > 1)
        {
            for (int i = 0; i < n / 2; ++i)
            {
                lists[i] = mergeTwoLists(lists[i], lists[n - 1 - i]);
            }
            n = (n + 1) / 2;
        }

        return lists[0];
    }
};
