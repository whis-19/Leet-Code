class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        
        for char in s:
            if char == ')':
                # Start popping until we find a '('
                substring = []
                while stack and stack[-1] != '(':
                    substring.append(stack.pop())
                # Pop the '(' from the stack
                if stack:
                    stack.pop()
                # Push the reversed substring back onto the stack
                stack.extend(substring)
            else:
                stack.append(char)
        
        # Join the characters to form the final result
        return ''.join(stack)