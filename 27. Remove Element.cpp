class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int j = 0; // Initialize the second pointer

        // Iterate through the array
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] != val)
            {
                nums[j] = nums[i];
                j++;
            }
        }

        return j;
    }
};
