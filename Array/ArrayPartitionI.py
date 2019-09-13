class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #336ms
        #return sum(sorted(nums)[::2])
        
        #332ms
        nums.sort()
        sum_num = 0
        for i in range(0,len(nums),2):
            sum_num += nums[i]
        return sum_num
