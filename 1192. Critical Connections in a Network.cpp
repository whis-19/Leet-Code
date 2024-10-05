class Solution
{
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>> &connections)
    {
        // Initialize graph as an adjacency list
        vector<vector<int>> graph(n);
        for (const auto &connection : connections)
        {
            graph[connection[0]].push_back(connection[1]);
            graph[connection[1]].push_back(connection[0]);
        }

        // Vectors to store discovery time and low value of each node
        vector<int> discovery(n, -1), low(n, -1);
        vector<vector<int>> bridges; // To store the critical connections
        int time = 0;                // Discovery time counter

        // Helper function for DFS
        function<void(int, int)> dfs = [&](int node, int parent)
        {
            discovery[node] = low[node] = time++;
            for (int neighbor : graph[node])
            {
                if (neighbor == parent)
                    continue;
                if (discovery[neighbor] == -1)
                {
                    dfs(neighbor, node);
                    low[node] = min(low[node], low[neighbor]);
                    if (low[neighbor] > discovery[node])
                    {
                        bridges.push_back({node, neighbor});
                    }
                }
                else
                {
                    low[node] = min(low[node], discovery[neighbor]);
                }
            }
        };

        // Run DFS from the first node
        dfs(0, -1);

        return bridges;
    }
};