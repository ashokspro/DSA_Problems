#initially generates a list and then appending it with adding before and the current number
#return the number with the location as n
class Solution:
    def nthFibonacci(self, n: int) -> int:
        fib = [0,1]
        
        for i in range(1,n+1):
            fib.append(fib[i-1]+fib[i])
        return fib[n]
        
"""another method 


class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        a, b = 0, 1
        for i in range(2,n+1):
            a, b = b , a+b
        
        return b if n > 0 else a
        


"""