class Solution {
public:
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        int n = scores.size();
        
        // Adjacency list representation
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        // Priority queue to store the top 3 highest scoring neighbors
        vector<priority_queue<pair<int, int>>> top3(n);
        for (int i = 0; i < n; ++i) {
            for (int neighbor : adj[i]) {
                top3[i].emplace(scores[neighbor], neighbor);
                if (top3[i].size() > 3) {
                    top3[i].pop();
                }
            }
        }

        int maxScore = -1;
        
        // Iterate over each edge to form sequences
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];

            // Consider each pair of neighbors (u-neigh_u and v-neigh_v)
            for (const auto& [scoreU, neighU] : top3[u]) {
                if (neighU == v) continue;
                for (const auto& [scoreV, neighV] : top3[v]) {
                    if (neighV == u || neighV == neighU) continue;
                    int currentScore = scores[u] + scores[v] + scoreU + scoreV;
                    maxScore = max(maxScore, currentScore);
                }
            }
        }

        return maxScore;
    }
};
