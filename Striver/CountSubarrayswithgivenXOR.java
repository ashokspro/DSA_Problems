class Solution {
    public long subarrayXor(int arr[], int k) {
        // code here
        int prev = 0, res = 0;
        HashMap<Integer,Integer> hash = new HashMap<>();
        hash.put(0, 1);
        for (int a: arr){
            prev ^= a;
            int pre = prev ^ k;
            int v = hash.getOrDefault(pre, 0);
            res += v;
            hash.put(prev, hash.getOrDefault(prev, 0) + 1);
        }
        return res;
        
    }
}