class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2): #function that finds the median of two sorted arrays.
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2) #Merge the two sorted arrays and sort the result.
        n = len(merged) #Calculate the length of the merged array.
    
        if n % 2 == 1: #If the length is odd, return the middle element.
            return float(merged[n // 2]) #If the length is even, return the average of the two middle elements.
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0 #This function returns the median of two sorted arrays nums1 and nums2.
        