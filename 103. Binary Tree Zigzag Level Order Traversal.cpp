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
    vector<vector<int>> zigzagLevelOrder(TreeNode *root)
    {
        vector<vector<int>> result;
        if (!root)
            return result; // If the tree is empty, return an empty result

        deque<TreeNode *> dq;
        dq.push_back(root);
        bool leftToRight = true; // Start with left to right

        while (!dq.empty())
        {
            int levelSize = dq.size(); // Number of nodes at the current level
            vector<int> currentLevel;

            for (int i = 0; i < levelSize; ++i)
            {
                if (leftToRight)
                {
                    TreeNode *currentNode = dq.front();
                    dq.pop_front();
                    currentLevel.push_back(currentNode->val);

                    if (currentNode->left)
                        dq.push_back(currentNode->left);
                    if (currentNode->right)
                        dq.push_back(currentNode->right);
                }
                else
                {
                    TreeNode *currentNode = dq.back();
                    dq.pop_back();
                    currentLevel.push_back(currentNode->val);

                    if (currentNode->right)
                        dq.push_front(currentNode->right);
                    if (currentNode->left)
                        dq.push_front(currentNode->left);
                }
            }

            result.push_back(currentLevel);
            leftToRight = !leftToRight; // Alternate the direction
        }

        return result;
    }
};