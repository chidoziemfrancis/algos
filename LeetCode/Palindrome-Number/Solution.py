1
2class Solution:
3    def isPalindrome(self, x: int) -> bool:
4        original = str(x)
5        reverse = original[::-1]
6        return original == reverse