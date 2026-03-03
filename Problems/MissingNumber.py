class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = (n * (n + 1)) // 2
        return exp_sum - sum(nums)
    
#brute force 
"""class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
"""