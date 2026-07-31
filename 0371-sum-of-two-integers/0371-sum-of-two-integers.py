class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        while (b & MASK) > 0:
            carry = (a & b) <<  1
            a = a ^ b
            b = carry
        if b > 0:
            return (a & MASK)
        else:
            return a
        