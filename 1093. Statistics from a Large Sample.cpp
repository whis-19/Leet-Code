class Solution
{
public:
    vector<double> sampleStats(vector<long long> &count)
    {
        long long n = count.size();
        long long total_elements = 0;
        double total_sum = 0.0;
        long long min_value = -1;
        long long max_value = -1;
        long long mode_value = -1;
        long long mode_frequency = 0;

        for (long long i = 0; i < n; ++i)
        {
            if (count[i] > 0)
            {
                if (min_value == -1)
                {
                    min_value = i;
                }
                max_value = i;
                total_elements += count[i];
                total_sum += i * count[i];
                if (count[i] > mode_frequency)
                {
                    mode_frequency = count[i];
                    mode_value = i;
                }
            }
        }

        double mean = total_sum / total_elements;

        // Finding the median
        double median;
        long long mid = total_elements / 2;
        if (total_elements % 2 == 0)
        {
            long long first = -1, second = -1;
            long long current_count = 0;
            for (long long i = 0; i < n; ++i)
            {
                current_count += count[i];
                if (first == -1 && current_count >= mid)
                {
                    first = i;
                }
                if (second == -1 && current_count >= mid + 1)
                {
                    second = i;
                    break;
                }
            }
            median = (first + second) / 2.0;
        }
        else
        {
            long long current_count = 0;
            for (long long i = 0; i < n; ++i)
            {
                current_count += count[i];
                if (current_count > mid)
                {
                    median = i;
                    break;
                }
            }
        }

        return {static_cast<double>(min_value), static_cast<double>(max_value), mean, median, static_cast<double>(mode_value)};
    }
};