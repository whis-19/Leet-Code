class Solution
{
public:
    bool judgeSquareSum(int c)
    {
        for (long int a = 0; a * a <= c; ++a)
        {
            long int b = c - a * a;
            long int sqrt_b = static_cast<long int>(sqrt(b));
            if (sqrt_b * sqrt_b == b)
            {
                return true;
            }
        }
        return false;
    }
};