class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,el in enumerate(nums):
            if el >= target:
                return i
        return len(nums)
