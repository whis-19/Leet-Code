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
    bool isSymmetric(TreeNode *root)
    {
        if (!root)
            return true; // An empty tree is symmetric
        return isMirror(root->left, root->right);
    }

private:
    bool isMirror(TreeNode *left, TreeNode *right)
    {
        if (!left && !right)
            return true; // Both subtrees are empty
        if (!left || !right)
            return false; // Only one subtree is empty

        // Check if current nodes have the same value and
        // the left subtree of the left node is a mirror of the right subtree of the right node
        // and the right subtree of the left node is a mirror of the left subtree of the right node
        return (left->val == right->val) && isMirror(left->left, right->right) && isMirror(left->right, right->left);
    }
};
