class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        res = []
        for i in range(len(arr) - 1):
            curr = arr[i + 1] - arr[i]
            if curr < min_diff:
                min_diff = curr
                res = []
            if curr == min_diff:
                res.append([arr[i], arr[i + 1]])

        return res
