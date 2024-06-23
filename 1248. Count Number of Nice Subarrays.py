class Solution(object):
    def numberOfSubarrays(self, nums, k):
        # Transform nums into odd_count where odd numbers are 1 and even numbers are 0
        odd_count = [1 if num % 2 != 0 else 0 for num in nums]
        
        # Initialize variables
        prefix_sum = 0
        count_map = {0: 1}  # to handle subarrays starting from index 0
        result = 0
        
        # Traverse through odd_count and calculate the number of subarrays
        for num in odd_count:
            prefix_sum += num
            # If prefix_sum - k has been seen before, add its count to result
            if prefix_sum - k in count_map:
                result += count_map[prefix_sum - k]
            # Update count_map with current prefix_sum
            if prefix_sum in count_map:
                count_map[prefix_sum] += 1
            else:
                count_map[prefix_sum] = 1
        
        return result

