class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count+1
        return count;