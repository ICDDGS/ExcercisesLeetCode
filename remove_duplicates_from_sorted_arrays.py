class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in nums:
            if j != nums[i]:
                nums[i+1] = j
                i+=1
        return i+1


solution = Solution()
nums = [1,1,1,1]
result = solution.removeDuplicates(nums)

print(result)