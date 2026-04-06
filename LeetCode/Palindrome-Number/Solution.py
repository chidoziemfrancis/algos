1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        original = str(x)
4        reverse = original[::-1]
5        return original == reverse
6