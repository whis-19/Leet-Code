class Solution
{
public:
    string countOfAtoms(string formula)
    {
        map<string, int> counts = parseFormula(formula);
        string result;
        for (auto &[elem, cnt] : counts)
        {
            result += elem;
            if (cnt > 1)
                result += to_string(cnt);
        }
        return result;
    }

private:
    map<string, int> parseFormula(const string &formula)
    {
        stack<map<string, int>> stack;
        stack.push(map<string, int>());
        int n = formula.size();

        for (int i = 0; i < n;)
        {
            if (formula[i] == '(')
            {
                stack.push(map<string, int>());
                i++;
            }
            else if (formula[i] == ')')
            {
                map<string, int> top = stack.top();
                stack.pop();
                i++;
                int i_start = i;
                while (i < n && isdigit(formula[i]))
                    i++;
                int multiplicator = i > i_start ? stoi(formula.substr(i_start, i - i_start)) : 1;
                for (auto &[elem, cnt] : top)
                {
                    stack.top()[elem] += cnt * multiplicator;
                }
            }
            else
            {
                int i_start = i;
                i++;
                while (i < n && islower(formula[i]))
                    i++;
                string elem = formula.substr(i_start, i - i_start);
                i_start = i;
                while (i < n && isdigit(formula[i]))
                    i++;
                int cnt = i > i_start ? stoi(formula.substr(i_start, i - i_start)) : 1;
                stack.top()[elem] += cnt;
            }
        }

        return stack.top();
    }
};
