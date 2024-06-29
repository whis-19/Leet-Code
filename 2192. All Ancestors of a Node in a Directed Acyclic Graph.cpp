class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        // Create adjacency list
        vector<vector<int>> adjList(n);
        vector<int> inDegree(n, 0);

        for (const auto& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            inDegree[edge[1]]++;
        }

        // Topological Sort using Kahn's Algorithm
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }

        vector<int> topoOrder;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            topoOrder.push_back(node);
            for (int neighbor : adjList[node]) {
                if (--inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        // Use DP to track ancestors
        vector<set<int>> ancestors(n);
        for (int node : topoOrder) {
            for (int neighbor : adjList[node]) {
                // Add current node as ancestor of neighbor
                ancestors[neighbor].insert(node);
                // Add all ancestors of current node to neighbor's ancestors
                ancestors[neighbor].insert(ancestors[node].begin(), ancestors[node].end());
            }
        }

        // Convert set to sorted vector
        vector<vector<int>> answer(n);
        for (int i = 0; i < n; ++i) {
            answer[i] = vector<int>(ancestors[i].begin(), ancestors[i].end());
        }

        return answer;
    }
};