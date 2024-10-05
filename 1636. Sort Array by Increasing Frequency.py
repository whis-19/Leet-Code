class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each number
        frequency = Counter(nums)
        # Step 2: Sort the numbers based on frequency and value
        sorted_nums = sorted(nums, key=lambda x: (frequency[x], -x))
        
        return sorted_nums