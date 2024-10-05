class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers to get permutations from
        numbers = list(range(1, n + 1))
        # Adjust k to be zero-indexed
        k -= 1
        # Initialize the result permutation list
        permutation = []
        
        # Calculate the factorial values needed for the positions
        factorial = math.factorial(n)
        
        # Generate the kth permutation
        for i in range(n, 0, -1):
            factorial //= i
            index = k // factorial
            permutation.append(str(numbers.pop(index)))
            k %= factorial
        
        return ''.join(permutation)

