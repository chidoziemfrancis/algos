1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3
4        num = int("".join(map(str, digits)))
5
6        num += 1
7
8        return [int(d) for d in str(num)]
9        
10