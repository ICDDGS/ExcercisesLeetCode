
diccRoman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.upper()
        count = 0
        last = 0
        for lettter in (s):
            if(last >= diccRoman[lettter]):
                ##print(diccRoman[lettter])
                count += diccRoman[lettter]
            else:
                count -= last
                count += diccRoman[lettter]-last
            last = diccRoman[lettter]
        return count

solution = Solution()
result = solution.romanToInt("MCMXCIV")

print(result)