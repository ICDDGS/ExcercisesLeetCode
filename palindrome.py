class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        for i in range (0,len(str(x))//2):
            if(x[i]!=x[-i-1]):

                return False
        return True

x = -121
solution = Solution()

result = solution.isPalindrome(x)
print(result)
