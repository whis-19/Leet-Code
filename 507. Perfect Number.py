class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        sum_divisors = 1
        sqrt_num = int(num**0.5)

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i

        return sum_divisors == num