class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int ct1 = 0;
        int ct2 = 0;
        int el1 = 0;
        int el2 = 0;

        for(int i = 0; i < nums.length; i++){
            if (ct1 == 0 && el2 != nums[i]) {
                ct1 = 1;
                el1 = nums[i];
            }
            else if (ct2 == 0 && el1 != nums[i]){ 
                ct2 = 1; 
                el2 = nums[i];
                }
            else if (el1 == nums[i]) ct1++;
            else if (el2 == nums[i]) ct2++;

            else{
                ct1--;
                ct2--;
            }
        }

        int ctt1 = 0;
        int ctt2 = 0;

        for(int i=0; i < nums.length; i++){
            if (nums[i] == el1) ctt1++;
            if (nums[i] == el2) ctt2++;

        }

        List<Integer> res = new ArrayList<>();

        if (ctt1 > (nums.length / 3)) res.add(el1);
        if ((ctt2 > (nums.length / 3)) && ((el1 != el2))) res.add(el2);
        return res;

    }
}