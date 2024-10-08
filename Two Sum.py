

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        print(hashmap)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
            print(hashmap)

solution = Solution()

lista = [3,2,4]

result = solution.twoSum(lista, 6)

print(result)
