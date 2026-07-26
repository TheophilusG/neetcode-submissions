class Solution:
    def search(self, nums: List[int], target: int) -> int:

        total_size = len(nums)
        left = 0
        right= total_size-1

        while left < right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle 
            
            elif nums[middle] > target:
                right = middle-1
            
            elif nums[middle] < target:
                left = middle+1
        
        return -1
        




        