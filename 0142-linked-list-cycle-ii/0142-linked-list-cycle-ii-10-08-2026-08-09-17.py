# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        # M-1
        # temp = head
        # s = set()
        # while temp is not None:
        #     if temp in s:
        #         return temp
        #     s.add(temp)
        #     temp = temp.next
        # return None

        # M-2
        slow  = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None