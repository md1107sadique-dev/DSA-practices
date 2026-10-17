class Solution(object):
    def reverseBetween(self, head, left, right):
        if head == None or head.next == None or left == right:
            return head
            
        temp = head
        prev = None
        pos = 1  # <--- Position counter add kiya
        
        while temp != None:
            if pos == left:  # <--- Value ki jagah position check karo
                x = prev
                z = temp
                prev = None
                count = 0
                
                # Exactly (right - left + 1) nodes reverse karo
                while temp is not None and count < (right - left + 1):
                    front = temp.next
                    temp.next = prev
                    prev = temp
                    temp = front
                    count += 1
                    
                if x is None:
                    head = prev 
                else:
                    x.next = prev
                    
                z.next = temp
                return head
            else:
                prev = temp 
                temp = temp.next
                pos += 1  # <--- Har step pe position badhao
                
        return head