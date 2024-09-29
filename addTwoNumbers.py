# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ll = ListNode()
        add_1 = False
        head = sum_ll
        while l1 is not None and l2 is not None:
            next_node = ListNode()
            next_node.val = l1.val + l2.val
            if add_1:
                next_node.val += 1
            if next_node.val > 9:
                add_1 = True
                next_node.val = next_node.val % 10
            else:
                add_1 = False

            sum_ll.next = next_node
            sum_ll = sum_ll.next

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            next_node = ListNode(l1.val, None)
            if add_1:
                next_node.val += 1
                if next_node.val > 9:
                    next_node.val = next_node.val % 10
                else:
                    add_1 = False
            sum_ll.next = next_node
            sum_ll = sum_ll.next
            l1 = l1.next
        while l2 is not None:
            next_node = ListNode(l2.val, None)
            if add_1:
                next_node.val += 1
                if next_node.val > 9:
                    next_node.val = next_node.val % 10
                else:
                    add_1 = False
            sum_ll.next = next_node
            sum_ll = sum_ll.next
            l2 = l2.next

        if add_1:
            sum_ll.next = ListNode(1, None)

        return head.next



