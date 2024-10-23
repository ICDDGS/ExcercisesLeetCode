class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ## join se encarga de unir los numeros del array
        ## map se encarga de convertir cada valor del array en un string
        digits =  int("".join(map(str,digits)))+1
        digits = str(digits).replace(""," ").split()
        return list(map(int,digits))
        


digits = [1,2,3]
solution = Solution()
res = solution.plusOne(digits)
print(res)