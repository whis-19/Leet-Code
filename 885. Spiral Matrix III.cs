public class Solution {
    public int[][] SpiralMatrixIII(int rows, int cols, int rStart, int cStart) {
		int cells = rows * cols;
        int[][] result = new int[cells][];
		int[][] direction = new int[][] { new int[] { 0, 1 }, new int[] { 1, 0 }, new int[] { 0, -1 }, new int[] { -1, 0 } };

		int step = 1;
		int count = 0;
		int turn = 0;
		int row = rStart;
		int col = cStart;
		while (count < cells){
			for (int move = 0; move < step; move++){
				if (row >= 0 && row < rows && col >= 0 && col < cols)
					result[count++] = new int[]{row, col};
		
				row += direction[turn][0];
				col += direction[turn][1];
			}
			turn = (turn + 1) % 4;
			if (turn == 0 || turn == 2)
				step++;
		}
		return result;
    }
}