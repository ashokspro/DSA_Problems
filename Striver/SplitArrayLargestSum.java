public class SplitArrayLargestSum {
    public int splitArray(int[] nums, int k) {
        int left = -1, right = 0, mid;
        for (int i=0;i<nums.length;i++){
            left = Math.max(left, nums[i]);
            right += nums[i];
        }
        int ans = 0;
        while (left < right){
            int sum = 0, count = 1;
            mid = left + (right - left) / 2;
            for (int i=0;i<nums.length;i++){
                if (sum + nums[i] > mid){
                    count++;
                    sum = nums[i];
                }
                else{
                sum += nums[i];
                }
            }
            if (count > k){
                left = mid + 1;
            }
            else{
                right = mid;
            }

        }
        return left;
    }
}
