# first solution both space and time O(n)
# split the numbers and saving it on a list if o replace 5 then reuturns
# 2nd pure maths digit increases *10 by *10 and add it up with the last digit
class Solution:
    def convertFive(self, n):
        if n == 0:
            return 5
        """ nums = []
        
        while n > 0:
            last = n % 10
            if last == 0:
                last = 5
            nums.append(last)
            n //= 10
        nums.reverse()
        return int(''.join(map(str, nums)))
        
            """    
        result = 0
        digit = 1
        while n > 0:
            last = n % 10
            if last == 0:
                last = 5
            result += digit * last
            digit *= 10
            n //= 10
        return result