class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        found = set()
        for i in range(len(nums)):
            if nums[i] in found:
                return nums[i]
            else:
                found.add(nums[i])