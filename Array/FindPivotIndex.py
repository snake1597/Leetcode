class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current = 0
        for i in range(len(nums)):
            if current * 2 == total_sum - nums[i]:
                return i
            else:
                current += nums[i]    
        return -1
