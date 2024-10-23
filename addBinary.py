class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(max(len(a),len(b)))

a = "11", b = "1"
sol = Solution()
res = sol(a,b)
print(res)