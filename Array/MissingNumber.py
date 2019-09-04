class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        num_len = len(nums) + 1
        for i in range(num_len):
            if i not in num_set:
                return i
