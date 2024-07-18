/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    int countPairs(TreeNode *root, int distance)
    {
        int result = 0;
        dfs(root, distance, result);
        return result;
    }

private:
    vector<int> dfs(TreeNode *node, int distance, int &result)
    {
        if (!node)
            return {};

        // If it's a leaf node, return a vector containing only the distance 1
        if (!node->left && !node->right)
            return {1};

        // Get distances from left and right children
        vector<int> leftDistances = dfs(node->left, distance, result);
        vector<int> rightDistances = dfs(node->right, distance, result);

        // Count good pairs between left and right distances
        for (int ld : leftDistances)
        {
            for (int rd : rightDistances)
            {
                if (ld + rd <= distance)
                {
                    result++;
                }
            }
        }

        // Collect the current distances for non-leaf nodes
        vector<int> currentDistances;
        for (int ld : leftDistances)
        {
            if (ld + 1 <= distance)
                currentDistances.push_back(ld + 1);
        }
        for (int rd : rightDistances)
        {
            if (rd + 1 <= distance)
                currentDistances.push_back(rd + 1);
        }

        return currentDistances;
    }
};