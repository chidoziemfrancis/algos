1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for num in nums:
6            if num in seen:
7                return True
8                break
9            seen.add(num)
10        else:
11            return False
12