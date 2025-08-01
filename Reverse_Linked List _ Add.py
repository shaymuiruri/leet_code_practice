class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get the current values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10

            # Create new node with the digit part
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
