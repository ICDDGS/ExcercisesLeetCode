class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        pos = 0
        for i,j in zip(range(1,len(s)),s):
            if j == " ":
                pos = i
        return len(s)-pos

s = "   fly me   to   the moon  "
solution = Solution()
res = solution.lengthOfLastWord(s)
print(res)
