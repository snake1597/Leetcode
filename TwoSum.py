class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i in range(0,len(nums)):
            if target - nums[i] in table:
                return [table[target - nums[i]],i]
            table[nums[i]] = i
