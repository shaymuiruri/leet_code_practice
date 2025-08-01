<<<<<<< HEAD
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                n = len(s) // 2
                left_sum = sum(int(d) for d in s[:n])
                right_sum = sum(int(d) for d in s[n:])
                if left_sum == right_sum:
                    count += 1
        return count

=======
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                n = len(s) // 2
                left_sum = sum(int(d) for d in s[:n])
                right_sum = sum(int(d) for d in s[n:])
                if left_sum == right_sum:
                    count += 1
        return count

>>>>>>> origin/main
        