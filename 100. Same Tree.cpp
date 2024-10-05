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
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        // If both nodes are null, they are the same
        if (p == nullptr && q == nullptr)
        {
            return true;
        }

        // If one node is null and the other is not, they are not the same
        if (p == nullptr || q == nullptr)
        {
            return false;
        }

        // If the values of the nodes are different, they are not the same
        if (p->val != q->val)
        {
            return false;
        }

        // Recursively check the left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};