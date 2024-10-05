class Solution
{
public:
    int findTheCity(int n, vector<vector<int>> &edges, int distanceThreshold)
    {
        // Step 1: Initialize the distance matrix with infinities
        vector<vector<int>> dist(n, vector<int>(n, INT_MAX));

        // Step 2: Build the initial distance matrix from the edges
        for (const auto &edge : edges)
        {
            int fromi = edge[0], toi = edge[1], weighti = edge[2];
            dist[fromi][toi] = weighti;
            dist[toi][fromi] = weighti;
        }

        // Initialize the distance of a city to itself to 0
        for (int i = 0; i < n; ++i)
        {
            dist[i][i] = 0;
        }

        // Step 3: Floyd-Warshall Algorithm to find all-pairs shortest paths
        for (int k = 0; k < n; ++k)
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX)
                    {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }

        // Step 4: Count reachable cities within distanceThreshold for each city
        int min_count = n + 1;
        int min_city = -1;

        for (int i = 0; i < n; ++i)
        {
            int count = 0;
            for (int j = 0; j < n; ++j)
            {
                if (i != j && dist[i][j] <= distanceThreshold)
                {
                    count++;
                }
            }
            if (count <= min_count)
            {
                min_count = count;
                min_city = i;
            }
        }

        return min_city;
    }
};