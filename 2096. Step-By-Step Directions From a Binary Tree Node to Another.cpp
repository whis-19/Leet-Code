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
    bool findPath(TreeNode *root, int value, string &path)
    {
        if (!root)
            return false;
        if (root->val == value)
            return true;

        path.push_back('L');
        if (findPath(root->left, value, path))
            return true;
        path.pop_back();

        path.push_back('R');
        if (findPath(root->right, value, path))
            return true;
        path.pop_back();

        return false;
    }

    string getDirections(TreeNode *root, int startValue, int destValue)
    {
        string startPath, destPath;

        findPath(root, startValue, startPath);
        findPath(root, destValue, destPath);

        int i = 0;
        while (i < startPath.size() && i < destPath.size() && startPath[i] == destPath[i])
        {
            i++;
        }

        string upSteps(startPath.size() - i, 'U');
        string downSteps = destPath.substr(i);

        return upSteps + downSteps;
    }
};
