public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int[] result = new int[2];
        result[0] = FindPosition(nums, target, true);  // Find the start position
        result[1] = FindPosition(nums, target, false); // Find the end position
        return result;
    }
    
    private int FindPosition(int[] nums, int target, bool findStart) {
        int left = 0, right = nums.Length - 1;
        int position = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else { // nums[mid] == target
                position = mid;
                if (findStart) {
                    right = mid - 1; // Continue searching towards the left for the start position
                } else {
                    left = mid + 1;  // Continue searching towards the right for the end position
                }
            }
        }
        
        return position;
    }
}
