class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(arr)):
            if (down and arr[i-1] < arr[i]) or (arr[i-1] == arr[i]):
                up = down = 0

            if arr[i] > arr[i-1]:
                up += 1

            if arr[i] < arr[i-1]:
                down += 1

            if up and down:
                res = max(res, up + down + 1)           


        return res
 