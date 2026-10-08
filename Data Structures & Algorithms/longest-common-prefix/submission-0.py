class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = min(len(w) for w in strs)
        # n = len(min_length)
        m = len(strs)
        result = ""
        for i in range(n):
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