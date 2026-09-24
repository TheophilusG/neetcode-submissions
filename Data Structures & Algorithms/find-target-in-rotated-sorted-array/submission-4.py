class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1
        
        # left is the index of the first element == 0
        #right the index of the right most element == len(nums)-1
        
        while left <= right:
            middle = (left + right) // 2 #we need to recompute the middle 
            if nums[middle] == target:
                return middle         
            #left sorted portion 
            elif nums[middle] >= target: # why >= 
                left = middle +1
            # right sorted portion
            else:
                right= middle - 1
        return -1

        
        # for index, element in enumerate(nums):




       
        