class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0;
        count = 0;
        for i in range(0,len(nums)):
            if nums[i] != nums[count]:
                count = count+1
                nums[count] = nums[i]
        return count+1