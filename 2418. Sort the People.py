class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = list(zip(names, heights))
        
        # Sort the combined list by heights in descending order
        combined.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        sorted_names = [name for name, height in combined]
        
        return sorted_names