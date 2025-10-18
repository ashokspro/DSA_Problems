# initially finding the length of the number
# looping through the number as a string calculating sum 

class Solution:
    def armstrongNumber (self, n):
        digit = len(str(n))
        sum_ = 0
        for num in str(n):
            sum_ += int(int(num)**digit)
        return True if sum_ == n else False
        