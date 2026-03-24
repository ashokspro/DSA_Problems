class Solution {
    public int minDays(int[] bloomDay, int m, int k) {

        if (bloomDay.length < (long) m * k){
            return -1;
        }

        int left = Integer.MAX_VALUE;
        int right = Integer.MIN_VALUE;

        for (int i=0; i < bloomDay.length; i++){
            left = Math.min(left, bloomDay[i]);
            right = Math.max(right, bloomDay[i]);

        }


        while (left <= right){
            int mid = left + (right - left) / 2;

            boolean days = isPossible(bloomDay, m, k, mid);

            if (!days){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }

        return left;

        
    }


    public boolean isPossible(int[] bloomDay, int m, int k, int days){
        int count = 0;
        int b = 0;
        for (int i=0; i<bloomDay.length; i++){
            if (bloomDay[i] <= days) count++;
            else{
                b += count / k ;
                count = 0;
            }

        }

        b += count / k;
        if (b >= m) return true;
        else return false;

    }



}