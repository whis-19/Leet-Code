class Solution
{
public:
    double myPow(double x, int n)
    {
        if (n == 0)
            return 1;

        double half = pow(x, n / 2);

        if (n % 2 == 0)
            return half * half;
        else
        {
            if (n > 0)
                return x * half * half;
            else
            {
                return (half * half) / x;
            }
        }
    }
};