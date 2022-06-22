class Solution:
    """this code allowed me to achieve, as of 22/06/2022:
       Runtime: 32 ms, faster than 90.17% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 54.77% of Python3 online submissions for Middle of the Linked List."""
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
                :param head:
                :return:
                Given the head of a singly linked list, return the middle node of the linked list.
                If there are two middle nodes, return the second middle node.

    Strategy - two possibilities:
    1. explore all nodes to compute depth and then explore from the head to the middle of the list [commented]
    2. explore all nodes saving them on a list an then when the depth is know return the node in the desired position
                """
        node = head
        depth = 0
        valist = []
        while node:
            valist.append(node)
            node = node.next
            depth += 1
        return valist[int(depth / 2)]

"""     node = head
        depth = 0
        while node:
            node = node.next
            depth += 1
        for _ in range(int(depth / 2)):
            head = head.next
        return head"""