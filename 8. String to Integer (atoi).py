    # Step 1: Ignore leading whitespace
    i = 0
    n = len(s)
    
    while i < n and s[i] == ' ':
        i += 1
    
    # Step 2: Determine the sign
    sign = 1
    if i < n and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1
    
    # Step 3: Read the integer
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        
        # Check for overflow and handle it
        if result > (2**31 - 1 - digit) // 10:
            return 2**31 - 1 if sign == 1 else -2**31
        
        result = result * 10 + digit
        i += 1
    
    # Step 4: Apply the sign
    result *= sign
    
    # Step 5: Return the result within the 32-bit signed integer range
    return max(-2**31, min(result, 2**31 - 1))