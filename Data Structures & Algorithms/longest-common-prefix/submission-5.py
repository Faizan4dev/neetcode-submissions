class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = min(len(m) for m in strs)
        m = len(strs)
        result = ""
        
        for i in range(min_len):
            match = True
            for j in range(1,m):
                if strs[0][i] != strs[j][i]:
                    match = False
                    break
                
            if match:
                result += strs[0][i]
            else:
                break
                

        return result