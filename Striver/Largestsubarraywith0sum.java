package Striver;

import java.util.HashMap;
import java.util.Map;

public class Largestsubarraywith0sum {
    int maxLength(int arr[]) {
        // code here
        int left = 0;
        int right = 1;
        int curr_sum = 0;
        int max = 0;
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, -1);
        for (int i=0; i<arr.length; i++){
            curr_sum += arr[i];
            
            if (seen.containsKey(curr_sum)){
                int prev_idx = seen.get(curr_sum);
                max = Math.max(max, i - prev_idx);
                
            }
            else{
                seen.put(curr_sum, i);
            }
        }
            
        return max;
    }
}
