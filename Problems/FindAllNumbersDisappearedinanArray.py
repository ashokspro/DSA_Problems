class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1
        res = [] 
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res
    


    #using set

    class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        set_num = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_num:
                res.append(i)

        return res