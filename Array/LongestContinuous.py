class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        current = 1
        max_length = 0
        if not nums:
            return 0       
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                if current > max_length:
                    max_length = current
                current = 1
        return max(current,max_length)
