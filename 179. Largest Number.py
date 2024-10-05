class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert integers to strings
        nums_str = list(map(str, nums))     
        # Step 2: Sort the numbers using a lambda function for comparison
        nums_str.sort(key=lambda x: x * 10, reverse=True)  # Multiply to ensure proper comparison
        # Step 3: Join the sorted strings
        largest_num = ''.join(nums_str)        
        # Step 4: Handle the case where the largest number is '0'
        return largest_num if largest_num[0] != '0' else '0'

