class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stack;

        for (char ch : s)
        {
            if (ch == '(' || ch == '{' || ch == '[')
            {
                stack.push(ch);
            }
            else
            {
                if (stack.empty())
                    return false;
                char topElement = stack.top();
                stack.pop();
                if ((ch == ')' && topElement != '(') ||
                    (ch == '}' && topElement != '{') ||
                    (ch == ']' && topElement != '['))
                {
                    return false;
                }
            }
        }

        return stack.empty();
    }
};
