class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashmaps = {}
        hashmapt = {}
        for i, c in enumerate(s):
            hashmaps[c] = i
        for i, c in enumerate(t):
            hashmapt[c] = i

        result = 0
        for c in s:
            result += abs(hashmaps[c] - hashmapt[c])
        return result