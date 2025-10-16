#find a new method to the sum of the digits untill it got to 1 digit 
# Digital Root Trick Formula  1 + (n-1) % 9 it gives the final answer

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num-1) % 9