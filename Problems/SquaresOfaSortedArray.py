class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l, r = 0, len(nums) - 1
        idx = r
        while l <= r:
            square_l = nums[l] * nums[l]
            square_r = nums[r] * nums[r]

            if square_l < square_r:
                result[idx] = square_r
                r -= 1
                idx -= 1
            else:
                result[idx] = square_l
                l += 1
                idx -= 1

        return result

        

