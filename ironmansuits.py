'''
first of all create a hashmap 
store the frequencies of the numbers 
get the largest 

'''
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        
        #hashmap to create char and how often it appears
        count = Counter(nums)
        
        #build a heap of top k elements and convert to output array
        return heapq.nlargest(k, count.keys(), key=count.get)
        