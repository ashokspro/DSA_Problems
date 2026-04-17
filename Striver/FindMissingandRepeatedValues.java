package Striver;

public class FindMissingandRepeatedValues {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n_len = grid.length;
        long n = (long)  n_len * n_len;
        
        long expectedSum = (long) ((n * (n+1)) / 2);
        long expectedSquare = (long) ((n * (n+1) * (2*n+1)) / 6);

        long actualSum = 0;
        long actualSquare = 0;
        for (int i=0; i<n_len; i++){
            for (int j=0; j<n_len; j++){
                actualSum += (long) grid[i][j];
                actualSquare += (long) grid[i][j] * grid[i][j];
            }
        }


        long diffSum = actualSum - expectedSum;
        long squareSum = actualSquare - expectedSquare;

        long sumAB = squareSum / diffSum;

        int a = (int) ((sumAB + diffSum) / 2);
        int b = (int) ((sumAB - diffSum) / 2);

        return new int[] {a, b};
    }
}
