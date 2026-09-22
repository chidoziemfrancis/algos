1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        
6        freq = {}
7
8        for char in s:
9            freq[char] = freq.get(char, 0) + 1
10        
11        for char in t:
12            if char not in freq:
13                return False 
14            
15            freq[char] -= 1
16
17            if freq[char] == 0:
18                del freq[char]
19        
20        return not freq