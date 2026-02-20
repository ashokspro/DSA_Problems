class Solution:
    def generate_row(self, n, r):
        arr = []
        ans = 1
        arr.append(ans)
        for i in range(1, r):
            ans *= n - i + 1
            ans //= i
            arr.append(int(ans))
        return arr

    def generate(self, numRows: int) -> List[List[int]]: 
        result = []

        for i in range(1, numRows + 1):
            row = self.generate_row(i - 1, i)
            result.append(row)

        return result
        