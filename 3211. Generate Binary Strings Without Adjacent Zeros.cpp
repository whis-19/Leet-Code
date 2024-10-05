class Solution
{
public:
    vector<string> validStrings(int n)
    {
        vector<string> result;
        backtrack("", n, result);
        return result;
    }

private:
    void backtrack(string curr_string, int remaining, vector<string> &result)
    {
        if (remaining == 0)
        {
            result.push_back(curr_string);
            return;
        }
        // Always allowed to append '0' if last character is not '0'
        if (curr_string.empty() || curr_string.back() != '0')
        {
            backtrack(curr_string + "0", remaining - 1, result);
        }
        // Always allowed to append '1'
        backtrack(curr_string + "1", remaining - 1, result);
    }
};
