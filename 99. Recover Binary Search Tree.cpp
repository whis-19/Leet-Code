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
    void inorder(TreeNode *root, TreeNode *&first, TreeNode *&second, TreeNode *&prev)
    {
        if (!root)
            return;

        // Traverse the left subtree
        inorder(root->left, first, second, prev);

        // Process the current node
        if (prev && root->val < prev->val)
        {
            if (!first)
            {
                first = prev;
            }
            second = root;
        }
        prev = root;

        // Traverse the right subtree
        inorder(root->right, first, second, prev);
    }

    void recoverTree(TreeNode *root)
    {
        // Initialize pointers for the nodes to be swapped
        TreeNode *first = nullptr;
        TreeNode *second = nullptr;
        TreeNode *prev = nullptr;

        // In-order traversal to find the two nodes
        inorder(root, first, second, prev);

        // Swap the values of the two nodes
        if (first && second)
        {
            swap(first->val, second->val);
        }
    }
};