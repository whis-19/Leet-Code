public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int p1 = 0, p2 = nums.Length - 1;
        while (p1 <= p2) {
            int mid = (p1 + p2) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) p1 = mid + 1;
            else p2 = mid - 1;
        }
        return p1;
    }
}