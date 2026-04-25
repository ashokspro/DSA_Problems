class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int curr = 0;
        for (int n : nums) {
            if (curr < 0) {
                curr = 0;
            }
            curr += n;
            res = Math.max(curr, res);
        }
        return res;
    }
}