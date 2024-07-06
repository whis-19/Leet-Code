class Solution(object):
    def multiply(self, num1, num2):
        # Convert the input strings to integers
        int_num1 = int(num1)
        int_num2 = int(num2)
        
        # Multiply the integers
        product = int_num1 * int_num2
        
        # Convert the product back to a string
        return str(product)
            