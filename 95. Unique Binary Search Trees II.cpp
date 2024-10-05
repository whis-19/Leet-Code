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
    vector<TreeNode *> generateTrees(int n)
    {
        if (n == 0)
            return {};
        return generateTreesRecursive(1, n);
    }

    vector<TreeNode *> generateTreesRecursive(int start, int end)
    {
        if (start > end)
            return {nullptr};

        std::vector<TreeNode *> allTrees;
        for (int i = start; i <= end; ++i)
        {
            // Generate all left and right subtrees
            vector<TreeNode *> leftTrees = generateTreesRecursive(start, i - 1);
            vector<TreeNode *> rightTrees = generateTreesRecursive(i + 1, end);

            // Combine each left and right subtree with the current root
            for (TreeNode *left : leftTrees)
            {
                for (TreeNode *right : rightTrees)
                {
                    TreeNode *root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    allTrees.push_back(root);
                }
            }
        }
        return allTrees;
    }
};
