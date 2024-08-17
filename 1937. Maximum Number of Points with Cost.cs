public class Solution {
    public long MaxPoints(int[][] points) {
        long maxPoints = 0;
        var row = points.Length; 
        var col = points[0].Length; 
        long[][] dp = new long[row][];

        for (int i = 0; i<row; i++) {
            dp[i] = new long[col];
        }

        for (int i=0; i<col;i++) {
            dp[0][i] = points[0][i];
        }

        // for each row, calculate the dp with max points.
        for (int i = 1; i< row; i++) {
            long[] prevRowDp = dp[i-1];
            
            // Get the largest values when going from left to right.
            long[] prevDpLTR = new long[col];
            prevDpLTR[0] = prevRowDp[0];
            for (int j = 1; j < col; j++) {
                prevDpLTR[j] = Math.Max(prevDpLTR[j-1] - 1, prevRowDp[j]);
            }

            // Get the largest values from going from right to left.
            long[] prevDpRtL = new long[col];
            prevDpRtL[col-1] = prevRowDp[col-1];
            for (int j = col-2; j >=0; j--) {
                prevDpRtL[j] = Math.Max(prevDpRtL[j+1] -1, prevRowDp[j]);
            }

            for (int j = 0; j < col; j++) {
                dp[i][j] = points[i][j] + Math.Max(prevDpLTR[j], prevDpRtL[j]);
            }
        }

        long[] lastRow = dp[row-1];
        foreach (var totalPoint in lastRow) {
            maxPoints = Math.Max(totalPoint, maxPoints);
        }
        return maxPoints;
    }
}