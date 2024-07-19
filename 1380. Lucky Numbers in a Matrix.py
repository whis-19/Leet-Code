class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row = {min(row) for row in matrix}
        
        max_in_col = {max(col) for col in zip(*matrix)}
        
        lucky_nums = list(min_in_row & max_in_col)
        
        return lucky_nums