class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write_index = 1  # Pointer to place the next allowed number
        count = 1  # To count occurrences of the current number

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index

