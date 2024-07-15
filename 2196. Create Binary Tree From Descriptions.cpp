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
    TreeNode *createBinaryTree(vector<vector<int>> &descriptions)
    {
        unordered_map<int, TreeNode *> nodes;
        unordered_set<int> children;

        for (const auto &desc : descriptions)
        {
            int parent_val = desc[0];
            int child_val = desc[1];
            bool is_left = desc[2];

            if (nodes.find(parent_val) == nodes.end())
            {
                nodes[parent_val] = new TreeNode(parent_val);
            }
            if (nodes.find(child_val) == nodes.end())
            {
                nodes[child_val] = new TreeNode(child_val);
            }

            TreeNode *parent_node = nodes[parent_val];
            TreeNode *child_node = nodes[child_val];

            if (is_left)
            {
                parent_node->left = child_node;
            }
            else
            {
                parent_node->right = child_node;
            }

            children.insert(child_val);
        }

        TreeNode *root = nullptr;
        for (const auto &pair : nodes)
        {
            if (children.find(pair.first) == children.end())
            {
                root = pair.second;
                break;
            }
        }

        return root;
    }
};