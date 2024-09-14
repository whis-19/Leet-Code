public class Solution {

    public static int longestSubarray(int[] nums) {
        int n = nums.length;
        
        int maxVal = nums[0];
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }
        
        int maxLen = 0;
        int currentLen = 0;
        
        for (int num : nums) {
            if (num == maxVal) {
                currentLen++;
            } else {
                currentLen = 0;
            }
            maxLen = Math.max(maxLen, currentLen);
        }
        
        return maxLen;
    }
}