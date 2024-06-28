class Solution
{
public:
    vector<long long> minOperations(vector<int> &nums, vector<int> &queries)
    {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        // Compute prefix sums
        vector<long long> prefixSums(n + 1, 0);
        for (int i = 0; i < n; ++i)
        {
            prefixSums[i + 1] = prefixSums[i] + nums[i];
        }

        vector<long long> result;
        result.reserve(queries.size());

        for (int q : queries)
        {
            // Binary search to find the insertion point of q in nums
            int pos = lower_bound(nums.begin(), nums.end(), q) - nums.begin();

            // Calculate operations required to make all elements equal to q
            long long leftSum = (long long)q * pos - prefixSums[pos];
            long long rightSum = (prefixSums[n] - prefixSums[pos]) - (long long)q * (n - pos);

            result.push_back(leftSum + rightSum);
        }

        return result;
    }
};