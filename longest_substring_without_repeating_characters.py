class Solution(object):
    def lengthOfLongestSubstring(self, s):#function that uses the sliding window technique to solve the longest substring without repetition problem.
        """
        :type s: str
        :rtype: int
        """
        seen = {}  #Dictionary / Hash map Stores each character as a key and its latest index as the value.
        left = max_len = 0 #left is the start index of the current window.
                           #max_len tracks the length of the longest valid substring found so far.

        for right in range(len(s)): #This is the sliding window loop. right is the window’s end
            if s[right] in seen and seen[s[right]] >= left: #checks for duplicate characters within the current window.
                left = seen[s[right]] + 1 #If a duplicate is found, move the left pointer to the right of the last occurrence of that character.
            seen[s[right]] = right #Update the hash map with the latest index of this character
            max_len = max(max_len, right - left + 1) #Calculate the length of the current substring and update max_len if it's larger than the previous max_len.

        return max_len #This function returns the length of the longest substring without repeating characters in the input string s.