class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        greatest = -1
        for i in range(len(arr) - 1, -1, -1):
            res[i]  = greatest
            if arr[i] > greatest:
                greatest = arr[i]
        return res
