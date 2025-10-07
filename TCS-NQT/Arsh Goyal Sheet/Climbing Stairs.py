# fibonacci series
# the location of the number in the fibonacci series is the ways that was availble
# we are adding the number  before -1 and -2 by "arr[i-1]+arr[i-2]"


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n]
