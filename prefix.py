class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""        
        prefijo = strs[0]
        for string in strs[1:]:
            while string[:len(prefijo)] != prefijo:
                print("s",string)
                print("p",prefijo)
                prefijo = prefijo[:-1]
                if not prefijo:
                    return ""
        
        return prefijo
solution = Solution()
strs = ["flower","flow","flight"]
result = solution.longestCommonPrefix(strs)

print(result)