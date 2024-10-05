class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        // Step 1: Calculate the degree of each city
        vector<int> degree(n, 0);
        for (const auto& road : roads) {
            degree[road[0]]++;
            degree[road[1]]++;
        }
        
        // Step 2: Sort the cities by their degrees
        vector<pair<int, int>> city_degree_pairs;
        for (int i = 0; i < n; ++i) {
            city_degree_pairs.emplace_back(degree[i], i);
        }
        sort(city_degree_pairs.rbegin(), city_degree_pairs.rend());
        
        // Step 3: Assign values to cities
        vector<int> importance_values(n);
        int current_value = n;
        for (const auto& p : city_degree_pairs) {
            importance_values[p.second] = current_value--;
        }
        
        // Step 4: Calculate the total importance
        long long total_importance = 0;
        for (const auto& road : roads) {
            total_importance += importance_values[road[0]] + importance_values[road[1]];
        }
        
        return total_importance;
        
    }
};