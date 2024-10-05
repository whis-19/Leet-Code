from typing import List
import sys

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        INF = float('inf')
        
        # Step 1: Initialize the cost matrix
        cost_matrix = [[INF] * 26 for _ in range(26)]
        
        # Cost of converting a character to itself is 0
        for i in range(26):
            cost_matrix[i][i] = 0
        
        # Step 2: Fill the cost matrix with given transformations
        for i in range(len(original)):
            orig_index = ord(original[i]) - ord('a')
            changed_index = ord(changed[i]) - ord('a')
            cost_matrix[orig_index][changed_index] = min(cost_matrix[orig_index][changed_index], cost[i])
        
        # Step 3: Apply Floyd-Warshall algorithm to find the minimum cost between all pairs of characters
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if cost_matrix[i][k] < INF and cost_matrix[k][j] < INF:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # Step 4: Calculate the total minimum cost to convert source to target
        total_cost = 0
        for i in range(n):
            s_index = ord(source[i]) - ord('a')
            t_index = ord(target[i]) - ord('a')
            if cost_matrix[s_index][t_index] == INF:
                return -1  # Impossible to transform
            total_cost += cost_matrix[s_index][t_index]
        
        return total_cost
