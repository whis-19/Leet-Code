class Solution
{
public:
    bool checkIfExist(vector<int> &arr)
    {
        std::unordered_set<int> seen;

        for (int num : arr)
        {
            if (seen.count(2 * num) > 0 || (num % 2 == 0 && seen.count(num / 2) > 0))
            {
                return true;
            }
            seen.insert(num);
        }

        return false;
    }
};