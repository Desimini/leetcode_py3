# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """this code allowed me to achieve, as of 09/07/2022:
    Runtime: 91 ms, faster than 66.4% of Python3 online submissions for Two Sum.
    Memory Usage: 14 MB, less than 43.8% of Python3 online submissions for Two Sum.
            """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param l1:
        :param l2:
        :return:
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Strategy:
        The units are handled separatedly to store the first node of the solution that will be returned and to handle
        the exceptional case of the remainder being certainly equal to 0.
        The remainder and the value of each node of the solution is calculated applying the divmod function to the
        sum of , (when present) the values of each node plus the remainder.
        Finally, if there is a residual remainder, that is added as last node.
        """
        p = ListNode()
        remainder, p.val = divmod(l1.val + l2.val, 10)
        l1 = l1.next
        l2 = l2.next
        unitsNode = p
        while l1 or l2:
            n = ListNode()
            x1 = 0
            x2 = 0
            if l1:
                x1 = l1.val
                l1 = l1.next
            if l2:
                x2 = l2.val
                l2 = l2.next
            remainder, n.val = divmod(x1 + x2 + remainder, 10)
            p.next = n
            p = n
        if remainder:
            n = ListNode()
            n.val = remainder
            p.next = n
        return unitsNode
