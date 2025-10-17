#finding the numbers which is divisible number 
#adding it and check whether both are same and return it


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_ = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                if i*i != num:
                    sum_ += i + num//i
                else:
                    sum_ += i
        return sum_ == num and num != 1