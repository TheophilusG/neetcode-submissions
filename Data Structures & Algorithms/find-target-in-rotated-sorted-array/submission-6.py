class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1
        
        # left is the index of the first element == 0
        #right the index of the right most element == len(nums)-1

        while left <= right:
            middle = (left + right) // 2 #we need to recompute the middle 
            if nums[middle] == target:
                return middle 

            #to check if we are in the left sorted portion 
            if nums[middle] >= nums[left]: 
                if target > nums[middle] or target < nums[left]:
                    #while we are on the left side 
                    #if target is > middle and less than the left most array we can no to do bs on the right side 

                    left = middle+1

                else:
                    right = middle -1
        
            elif nums[middle] > target: # why >= 
                left = middle +1

            # right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    middle = right - 1
                else:
                    middlet = left + 1


        return -1

        
        # for index, element in enumerate(nums):




       
        