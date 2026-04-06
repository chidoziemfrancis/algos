1"""
2Given an integer x, return true if x is a palindrome, and false otherwise.
3"""
4
5class Solution:
6    def isPalindrome(self, x: int) -> bool:
7        original = str(x)
8        reverse = original[::-1]
9        return original == reverse