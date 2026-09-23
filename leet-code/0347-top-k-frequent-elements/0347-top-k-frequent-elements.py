class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #build the frequency first 
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        print(frequency)

        #build a bucket list 

        bucket = [[] for _ in range(len(nums) + 1) ]

        for num in frequency:
            count = frequency[num] 
            bucket[count].append(num)

        #loop through the bucket list by reversing

        result = []

        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                result.append(num)
            
            if len(result) == k:
                return result 