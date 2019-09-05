class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Runtime 380ms
        return list(set(range(1,len(nums) + 1)) - set(nums))
    
        # Runtime 404ms
        #return set(range(1,len(nums)+1)).difference(set(nums))
        
        # Runtime 456ms
        # disappeared = list()
        # table = dict()
        # nums.sort()
        # for i in range(len(nums)):
        #     table[nums[i]] = nums[i]
        # for j in range(len(nums)):
        #     if j+1 not in table:
        #         disappeared.append(j+1)
        # return disappeared
