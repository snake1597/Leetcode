class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = dict()
        for i in range(len(nums)):
            if nums[i] in table:
                return True
            else:
                table[nums[i]] = nums[i]
        # use set()
        #if not nums:
	#  return False
	#return len(set(nums)) != len(nums)
