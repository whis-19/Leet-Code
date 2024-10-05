class Solution
{
public:
    // Helper function to perform in-order traversal and store the elements in a vector
    void inOrderTraversal(TreeNode *root, vector<int> &nodes)
    {
        if (root == nullptr)
            return;
        inOrderTraversal(root->left, nodes);
        nodes.push_back(root->val);
        inOrderTraversal(root->right, nodes);
    }

    // Helper function to convert sorted array to balanced BST
    TreeNode *sortedArrayToBST(vector<int> &nodes, int start, int end)
    {
        if (start > end)
            return nullptr;
        int mid = start + (end - start) / 2;
        TreeNode *node = new TreeNode(nodes[mid]);
        // Right Case
        node->left = sortedArrayToBST(nodes, start, mid - 1);
        // Left Case
        node->right = sortedArrayToBST(nodes, mid + 1, end);
        return node;
    }

    // Function to balance a BST
    TreeNode *balanceBST(TreeNode *root)
    {
        vector<int> nodes;
        inOrderTraversal(root, nodes);
        return sortedArrayToBST(nodes, 0, nodes.size() - 1);
    }
};
