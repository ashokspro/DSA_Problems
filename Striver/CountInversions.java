import java.util.ArrayList;

public class CountInversions {
    static int count = 0;
    static void merge(int arr[], int low, int mid, int high){
        ArrayList<Integer> temp = new ArrayList<>();
        int left = low;
        int right = mid+1;
        
        while (left <= mid && right <= high){
            if (arr[left] <= arr[right]){
                temp.add(arr[left]);
                left++;
            } 
            else{
                temp.add(arr[right]);
                count += (mid - left + 1);
                right++;
            }
        }
        
        while (left <= mid){
            temp.add(arr[left]);
            left++;
        }
        while (right <= high){
            temp.add(arr[right]);
            right++;
        }
        
        for (int i=low; i<=high; i++){
            arr[i] = temp.get(i - low);
        }
    }
    static void mS(int arr[], int low, int high){
        if (low >= high) return;
        int mid = (low + high) / 2;
        mS(arr, low, mid);
        mS(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
    static int inversionCount(int arr[]) {
        count = 0;
        mS(arr, 0, arr.length - 1);
        return count;
        
    }
}
