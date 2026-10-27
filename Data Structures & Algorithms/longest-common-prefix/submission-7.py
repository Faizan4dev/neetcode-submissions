class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = True
        n = min(len(st) for st in strs)
        res = ""
        for i in range(n):
            match = True
            for j in range(1,len(strs)):
                if strs[0][i] != strs[j][i]:
                    match = False
            if match:
                res +=strs[0][i]
            else:
                break
        
        return res

