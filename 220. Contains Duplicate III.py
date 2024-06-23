def binary_search_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
        
def binary_search_right(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo
        
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff < 1 or valueDiff < 0:
            return False
        

        window = []

        for i in range(len(nums)):
            # Check if there's a value in the window that satisfies the condition
            if window:
                pos1 = binary_search_left(window, nums[i] - valueDiff)
                pos2 = binary_search_right(window, nums[i] + valueDiff)
                if pos1 != pos2:
                    return True
            
            # Maintain the sorted order of the window
            pos = binary_search_right(window, nums[i])
            window.insert(pos, nums[i])
            
            # Ensure the size of the window remains <= indexDiff
            if i >= indexDiff:
                remove_pos = binary_search_left(window, nums[i - indexDiff])
                window.pop(remove_pos)
        
        return False

