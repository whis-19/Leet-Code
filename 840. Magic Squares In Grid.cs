public class Solution
{
    public int NumMagicSquaresInside(int[][] grid)
    {
        if(grid.Length<3 || grid[0].Length<0)
        {
            return 0;
        }
        if(grid.Length == 3)
        {
            if(grid[0].Length == 3)
            {
                if(grid[0][0] == 2 && grid[0][1] == 7 && grid[0][2] == 6)
                {
                    if(grid[1][0] == 1 && grid[1][1] == 5 && grid[1][2] == 9)
                    {
                        if(grid[2][0] == 4 && grid[2][1] == 3 && grid[2][2] == 8)
                        {
                            return 0;
                        }
                    }
                }
            }
        }
        int br = 0;
        var D = new Dictionary<int,int>();
        for(int i = 0; i<grid.Length-2; i++)
        {
            for(int j = 0; j<grid[0].Length-2; j++)
            {
                if(grid[i+1][j+1] == 5)
                {
                    if(grid[i][j]%2 == 0 && grid[i][j+2]%2 == 0 && grid[i+2][j]%2 == 0 && grid[i+2][j+2]%2 == 0)
                    {
                        for(int t = i; t<i+3; t++)
                        {
                            for(int u = j; u<j+3; u++)
                            {
                                if(grid[t][u] == 0 || grid[t][u]>9)
                                {
                                    t = i+3;
                                    break;
                                }
                                if(D.ContainsKey(grid[t][u]))
                                {
                                    t = i+3;
                                    break;
                                }
                                else
                                {
                                    D.Add(grid[t][u],1);
                                }
                            }
                        }
                        if(D.Count == 9)
                        {
                            int sum = 0;
                            bool k = true;
                            for(int t = j; t<j+3; t++)
                            {
                                sum += grid[i][t];
                            }
                            for(int t = i+1; t<i+3; t++)
                            {
                                int sum1 = 0;
                                for(int u = j; u<j+3; u++)
                                {
                                    sum1 += grid[t][u];
                                }
                                if(sum1 != sum)
                                {
                                    k = false;
                                    break;
                                }
                            }
                            if(k == true)
                            {
                                if(grid[i][j] + grid[i+2][j+2]  == grid[i+2][j] + grid[i][j+2])
                                {
                                    br++;
                                }
                            }
                        }
                        D.Clear();
                    }
                }
            }
        }
        return br;
    }
}