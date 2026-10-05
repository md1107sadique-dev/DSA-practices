# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if head is None:
            return None
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        num = count // 2
        current = head
        n = 0
        while n < num:
            current = current.next
            n += 1
        return current
            

        