/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode BuildTree(int[] inorder, int[] postorder) {
        int inorderIndex = inorder.Length - 1;
        int postorderIndex = postorder.Length - 1;
        return BuildTreeHelper(inorder, postorder, ref inorderIndex, ref postorderIndex, null);
    }

    private TreeNode BuildTreeHelper(int[] inorder, int[] postorder, ref int inorderIndex, ref int postorderIndex, int? stopValue) {
        if (inorderIndex < 0 || inorder[inorderIndex] == stopValue) {
            return null;
        }

        TreeNode root = new TreeNode(postorder[postorderIndex]);
        postorderIndex--;

        root.right = BuildTreeHelper(inorder, postorder, ref inorderIndex, ref postorderIndex, root.val);
        inorderIndex--;
        root.left = BuildTreeHelper(inorder, postorder, ref inorderIndex, ref postorderIndex, stopValue);

        return root;
    }
}