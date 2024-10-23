class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
haystack ="Hola"
needle ="la"
solution = Solution()
res = solution.strStr(haystack,needle)