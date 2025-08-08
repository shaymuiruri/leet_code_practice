class Solution(object):
    def longestPalindrome(self, s): #function that finds the longest palindromic substring in a given string s.
        """
        :type s: str
        :rtype: str
        """
        def expand(left, right): #Helper function to expand around the center and find the longest palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]: #Expand as long as the characters at left and right are equal and within bounds.
                left -= 1 #Move left pointer to the left
                right += 1 #Move right pointer to the right
            return s[left+1:right]  #Return the substring from left+1 to right, which is the longest palindrome found in this expansion.
        
        result = ""     #Initialize result to store the longest palindrome found.
        for i in range(len(s)):     #Iterate through each character in the string as a potential center of a palindrome.
            # Check for odd length palindrome
            odd = expand(i, i)
            # Check for even length palindrome
            even = expand(i, i + 1)
            # Update result with longer palindrome
            result = max(result, odd, even, key=len)
        
        return result #This function returns the longest palindromic substring in the input string s.
