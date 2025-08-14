class Solution(object):
    def maxArea(self, height):
        # Start with the widest possible container:
        # one pointer at the far left, one at the far right.
        left, right = 0, len(height) - 1  

        # Keeps track of the best (largest) water area found so far.
        max_area = 0 
        
        # Keep going until the two pointers meet.
        while left < right:
            # The distance between the two lines.
            width = right - left  

            # The water level is limited by the shorter line.
            min_height = min(height[left], height[right])  

            # Calculate the current container's area and see if it's the best so far.
            max_area = max(max_area, width * min_height)
            
            # Move the pointer at the shorter line inward:
            # This is the only way to *possibly* increase height and area,
            # because moving the taller one won't help — width will shrink, height stays the same or less.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # After trying all pointer positions, return the largest area found.
        return max_area
