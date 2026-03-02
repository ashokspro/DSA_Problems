class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hm = {}
        sorted_nums = sorted((nums))
        res = []
        for i, num in enumerate(sorted_nums):
            if num not in hm:
                hm[num] = i

        for num in nums:
            res.append(hm[num])

        return res


# Brute Force
"""class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hm = {}
        # sorted_nums = sorted(nums)
        # n = len(nums)
        res = []
        for i in range(len(nums)):
            count = 0
            added = False
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    added = True
                    count += 1
            if not added:
                res.append(0)
            else:
                res.append(count)
            
        return res
            

"""