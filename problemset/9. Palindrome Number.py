"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reverse = original[::-1]
        return original == reverse