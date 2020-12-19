import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = -sys.maxsize - 1
        max = -sys.maxsize - 1
        
        for num in nums:
            after_add = current + num
            
            if after_add > num:
                current = after_add
            else:
                current = num
            
            if current > max:
                max = current
        return max
        