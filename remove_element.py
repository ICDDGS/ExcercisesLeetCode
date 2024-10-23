class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
            print(nums)
        print(nums)

nums = [3,2,2,3]
val = 3
solution = Solution()
res = solution.removeElement(nums,val)