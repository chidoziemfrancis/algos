1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        for i in range(len(nums)):
4            if nums[i] == target:
5                return i
6            if nums[i] > target:
7                return i
8        return len(nums)