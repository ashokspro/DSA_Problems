import math

class Solution:
    def FindRoots(self, A, B, C):
        if A == 0:
            return -1

        D = B * B - 4 * A * C

        if D < 0:
            return -1

        DSqrt = math.sqrt(D)
        r1 = (-B + DSqrt) / (2.0 * A)
        r2 = (-B - DSqrt) / (2.0 * A)

        if r1 > r2:
            r1, r2 = r2, r1

        return r1,r2
