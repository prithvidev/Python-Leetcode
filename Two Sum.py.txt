class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            h = target - nums[i]
            if h in d:
                return [d[h], i]
            d[nums[i]] = i