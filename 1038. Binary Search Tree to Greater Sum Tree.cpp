struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    void bstToGstHelper(TreeNode *root, int &sum)
    {
        if (!root)
            return;
        bstToGstHelper(root->right, sum);
        sum += root->val;
        root->val = sum;

        bstToGstHelper(root->left, sum);
    }

    TreeNode *bstToGst(TreeNode *root)
    {
        int sum = 0;
        bstToGstHelper(root, sum);
        return root;
    }
};