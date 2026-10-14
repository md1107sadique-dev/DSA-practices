# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        count = 0
        temp = head
        while temp != None:
            temp = temp.next
            count += 1
        main = count - n
        c = 0
        temp = head
        if main == 0:
            return head.next
        while temp != None and temp.next != None:
            if c == main-1:
                temp.next = temp.next.next
                return head
            temp = temp.next
            c += 1
        return head

        