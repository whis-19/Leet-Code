class Solution:
    def maximumLength(self, nums):
        all_zeroes = 0
        all_ones = 0
        zero_one = 0
        one_zero = 0
        reqd_for_zero_one = 0
        reqd_for_one_zero = 1
        
        for num in nums:
            new_num = num % 2
            
            if new_num == 0:
                all_zeroes += 1
            
            if new_num == 1:
                all_ones += 1
            
            if new_num == reqd_for_zero_one:
                zero_one += 1
                reqd_for_zero_one ^= 1
            
            if new_num == reqd_for_one_zero:
                one_zero += 1
                reqd_for_one_zero ^= 1
        
        return max(all_zeroes, all_ones, zero_one, one_zero)

