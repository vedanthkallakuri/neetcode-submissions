class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return abs(nums[i])
            else:
                nums[index] = -1 * nums[index]
            
    
    # 1 3 4 2 2
    # -1 3 4 2 2
    # -1 3 -4 2 2
    # -1 3 -4 -2 2
    # -1 -3 -4 -2 2
    # -1 -3 -4 -2 -2