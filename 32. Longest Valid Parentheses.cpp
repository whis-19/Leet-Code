class Solution
{
public:
    int longestValidParentheses(string s)
    {
        stack<int> stk;
        stk.push(-1); // Initialize stack with a dummy element
        int max_length = 0;

        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] == '(')
            {
                stk.push(i); // Push index of '(' onto stack
            }
            else
            {              // s[i] == ')'
                stk.pop(); // Pop the top element from stack

                if (stk.empty())
                {
                    stk.push(i); // No matching '(' found, push current index
                }
                else
                {
                    max_length = max(max_length, i - stk.top()); // Calculate current valid length
                }
            }
        }

        return max_length;
    }
};