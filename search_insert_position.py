class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0] or nums ==  None:
                return 0
            i = 1
            while target-i not in nums:
                i+=1
            return nums.index(target-i) + 1


nums = [-1,3,5,6]
target = 0
res = Solution().searchInsert(nums,target)

print(res)