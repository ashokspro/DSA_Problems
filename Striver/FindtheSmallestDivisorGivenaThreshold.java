public class FindtheSmallestDivisorGivenaThreshold  {
    public int smallestDivisor(int[] nums, int threshold) {
        int min = 1;
        int max = Integer.MIN_VALUE;
        for (int i=0; i<nums.length; i++){
            max = Math.max(max, nums[i]);
        }

        while (min <= max){
            
            int mid = min + (max-min) / 2;
            int num = 0;

            for (int i=0; i<nums.length; i++){
                num += (nums[i] + mid - 1) / mid;
            }
            if (num <= threshold){
                max = mid - 1;
            }
            else{
                min = mid + 1;
            }
        }
        return min;
               
    }
    
}
