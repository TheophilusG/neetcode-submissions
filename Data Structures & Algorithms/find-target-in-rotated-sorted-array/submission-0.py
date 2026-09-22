class Solution:
    def search(self, nums: List[int], target: int) -> int:
        decoy = nums[0]

        left, right = nums[0], len(nums)-1

        if decoy == target:
            return nums[0]
        
        middle = (left + right) // 2

        while left <= right:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                left = middle +1
            else:
                right= middle - 1

        
        # for index, element in enumerate(nums):




       
        