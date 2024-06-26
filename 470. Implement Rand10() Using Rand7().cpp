
class Solution
{
public:
    int rand10()
    {
        int num;
        while (true)
        {
            // Generate a number in the range [1, 49]
            int row = rand7();
            int col = rand7();
            num = (row - 1) * 7 + col;

            if (num <= 40)
                return num % 10 + 1;
        }
    }
};