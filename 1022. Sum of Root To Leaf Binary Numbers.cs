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
public class Solution
{
    public int SumRootToLeaf(TreeNode? root, int? number = 0)
    {
        number = number * 2 + root?.val;
        return root?.left is null && root?.right is null
            ? number ?? 0
            : SumRootToLeaf(root.left, number) + SumRootToLeaf(root.right, number);
    }
}