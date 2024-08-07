/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */

public class Solution {
    public TreeNode result;
    public void dfs(TreeNode root, int val){
        if(root!=null){
            if(root.val==val) result=root;
            dfs(root.left,val);
            dfs(root.right,val);
        }
    }
    public TreeNode GetTargetCopy(TreeNode original, TreeNode cloned, TreeNode target) {
        dfs(cloned, target.val);
        return result;
    }
}