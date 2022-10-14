# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = None
        t = None
        car = 0
        while l1 is not None or l2 is not None:
            sum_value = car
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
            node = ListNode(sum_value % 10)
            car = sum_value // 10
            if t is None:
                t = h = node
            else:
                t.next = node
                t = t.next
        if car > 0:
            t.next = ListNode(car)
        return h