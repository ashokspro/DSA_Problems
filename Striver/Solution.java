public class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt(); 

        while (left <= right){

            int mid = left + (right - left) / 2;
            long time_taken = hours(piles, mid);

            if (time_taken <= h){
                right = mid - 1;

            }else{
                left = mid + 1;
            }

        }

        return left;
        

    }



    public long hours(int[] piles, int k){
    long hour = 0;

    for (int i = 0; i < piles.length ; i++){
        hour += (piles[i] + k - 1) / k;

        if (hour > Integer.MAX_VALUE) return hour; 
    }

    return hour;
}
}