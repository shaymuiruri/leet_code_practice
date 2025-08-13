class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending in 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0 # Initialize the reversed half of the number
        while x > reversed_half: # Continue until the original number is greater than the reversed half
            reversed_half = reversed_half * 10 + x % 10 
            x //= 10
        
        # For even-length palindromes: x == reversed_half
        # For odd-length palindromes: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
