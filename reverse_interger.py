class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1 # Define the 32-bit signed integer range
        sign = -1 if x < 0 else 1 # Determine the sign of the input integer
        x *= sign # Work with the absolute value of x
        rev = 0 # Initialize the reversed integer
        
        # Reverse the integer digit by digit
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check overflow before adding digit
            if rev > (INT_MAX - digit) // 10:
                return 0
            
            rev = rev * 10 + digit # Append the digit to the reversed integer
        
        return sign * rev # Restore the sign and return the result
