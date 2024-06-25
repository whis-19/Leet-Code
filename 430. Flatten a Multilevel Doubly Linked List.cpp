/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution
{
public:
    Node *flatten(Node *head)
    {
        if (!head)
            return nullptr;

        stack<Node *> st;
        Node *curr = head;

        while (curr)
        {
            if (curr->child)
            {
                // If there is a next node, push it onto the stack
                if (curr->next)
                    st.push(curr->next);

                // Move the child to the next position
                curr->next = curr->child;
                if (curr->next)
                    curr->next->prev = curr;

                // Remove the child pointer
                curr->child = nullptr;
            }

            // If we reach the end of the current level and there are nodes in the stack
            if (!curr->next && !st.empty())
            {
                curr->next = st.top();
                st.pop();
                if (curr->next)
                    curr->next->prev = curr;
            }

            // Move to the next node
            curr = curr->next;
        }

        return head;
    }
};
