class Solution:
    def isNumber(self, s: str) -> bool:
    # Define the regular expression for a valid number
        number_regex = re.compile(r"""
            ^                           # start of string
            [+-]?                       # optional sign
            (                           # start of group for the number part
                (\d+\.\d*) |            # digits followed by dot, optional digits
                (\.\d+) |               # dot followed by digits
                (\d+(\.\d*)?)           # digits, optional dot and optional digits
            )
            ([eE][+-]?\d+)?             # optional exponent part
            $                           # end of string
        """, re.VERBOSE)

        # Use the regex to check if the string matches
        return bool(number_regex.match(s))     