class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_set = list(set(nums))
        num_set.sort()
        if len(num_set) < 3:
            return max(num_set)
        else:
            return num_set[-3]
            
