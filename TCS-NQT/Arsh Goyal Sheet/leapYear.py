# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.

class Solution:
    def checkYear (self, n):
        if n % 4 == 0:
            if n % 100 == 0:
                return n % 400 == 0
            return True
    
        return False