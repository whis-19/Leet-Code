class Solution
{
public:
    string crackSafe(int n, int k)
    {
        if (n == 1 && k == 1)
            return "0";
        string result;
        unordered_set<string> visited;
        string start(n - 1, '0');
        dfs(start, k, visited, result);
        result += start;
        return result;
    }

private:
    void dfs(const string &node, int k, unordered_set<string> &visited, string &result)
    {
        for (int i = 0; i < k; ++i)
        {
            string next = node + to_string(i);
            if (!visited.count(next))
            {
                visited.insert(next);
                dfs(next.substr(1), k, visited, result);
                result += to_string(i);
            }
        }
    }
};
