class Solution(object):
    def convert(self, s, numRows): # Function to convert a string into a zigzag pattern on a given number of rows and return it as a single string.
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
            # If the number of rows is 1 or greater than the length of the string, return the string as is
        if numRows == 1 or numRows >= len(s): 
            return s

        # Create an array of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Traverse the string and place each character in the correct row
        for char in s:
            rows[current_row] += char
            # Reverse direction if we are at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        # Join all rows to get the final string
        return ''.join(rows)
    