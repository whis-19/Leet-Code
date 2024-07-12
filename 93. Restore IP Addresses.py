class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)

        # Iterate through the first dot position
        for i in range(1, min(n, 4)):
            # Iterate through the second dot position
            for j in range(i + 1, min(n, i + 4)):
                # Iterate through the third dot position
                for k in range(j + 1, min(n, j + 4)):
                    if k < n:
                        segment1 = s[:i]
                        segment2 = s[i:j]
                        segment3 = s[j:k]
                        segment4 = s[k:]
                        
                        # Check if each segment is valid
                        if (len(segment1) == 1 or (segment1[0] != '0' and int(segment1) <= 255)) and \
                        (len(segment2) == 1 or (segment2[0] != '0' and int(segment2) <= 255)) and \
                        (len(segment3) == 1 or (segment3[0] != '0' and int(segment3) <= 255)) and \
                        (len(segment4) == 1 or (segment4[0] != '0' and int(segment4) <= 255)):
                            result.append(f"{segment1}.{segment2}.{segment3}.{segment4}")
        
        return result