class Solution(object):
    def find(self, parent, u):
        if parent[u] != u:
            parent[u] = self.find(parent, parent[u])
        return parent[u]
        
    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return True
        return False
        
    def maxNumEdgesToRemove(self, n, edges):
        # Initialize parent and rank arrays for Alice and Bob
        parent_alice = list(range(n))
        rank_alice = [1] * n
        parent_bob = list(range(n))
        rank_bob = [1] * n
        parent_shared = list(range(n))
        rank_shared = [1] * n
        
        added_edges = 0
        
        # Process type 3 edges first
        for edge_type, u, v in sorted(edges, key=lambda x: -x[0]):
            u -= 1  # Convert to 0-based index
            v -= 1  # Convert to 0-based index
            if edge_type == 3:
                if self.union(parent_shared, rank_shared, u, v):
                    self.union(parent_alice, rank_alice, u, v)
                    self.union(parent_bob, rank_bob, u, v)
                    added_edges += 1
            elif edge_type == 1:
                if self.union(parent_alice, rank_alice, u, v):
                    added_edges += 1
            elif edge_type == 2:
                if self.union(parent_bob, rank_bob, u, v):
                    added_edges += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if len(set(self.find(parent_alice, i) for i in range(n))) != 1 or len(set(self.find(parent_bob, i) for i in range(n))) != 1:
            return -1
        
        return len(edges) - added_edges
