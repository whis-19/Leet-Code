class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Create a function to map a number to its new value based on the mapping
        def map_number(num: int) -> int:
            mapped_num_str = ''.join(str(mapping[int(d)]) for d in str(num))
            return int(mapped_num_str)

        # Sort nums based on the mapped values
        return sorted(nums, key=map_number)