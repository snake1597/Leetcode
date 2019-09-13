class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        a = 0
        b = 0
        if operator.eq(nums,nums_sort) == False:
            for i in range(len(nums)):
                if nums[i] != nums_sort[i]:
                    a = i
                    break
            for i in range(len(nums)-1,0,-1):
                if nums[i] != nums_sort[i]:
                    b = i
                    break
            return b-a+1
        else:
            return 0
