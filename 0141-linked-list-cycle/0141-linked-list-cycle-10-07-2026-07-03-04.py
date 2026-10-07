# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return head
        
        # M - 1(Brute force)
        # z = set()
        # temp = head
        # while temp is not None:
        #     if temp in z:
        #         return True
        #     z.add(temp)
        #     temp = temp.next

        # M-2(Optimal)
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        