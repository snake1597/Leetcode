class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_num = current
        for i in range(1,len(nums)):  
            if nums[i] > current and 0 > current:
                current = nums[i]
            else:
                current += nums[i]
            max_num = max(current,max_num)
        return max_num
