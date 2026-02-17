class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        presum = 0

        for num in nums:
            presum += num

            if presum - k in hashmap:
                count += hashmap[presum - k]
            
            if presum not in hashmap:
                hashmap[presum] = 1
            else:
                hashmap[presum] += 1
        
        return count
