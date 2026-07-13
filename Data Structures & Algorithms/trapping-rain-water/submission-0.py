class Solution:
    def trap(self, height: List[int]) -> int:

        area = 0
        left, right = 0, len(height)-1

     
        while left < right:

            for i in height:

                if min(height[left], height[right]) - height[i] >= 0:
                    area+=min(height[left], height[right]) - height[i] >= 0

                if height[left] < height[right]:
                    left+=1
                elif height[right] < height[left]:
                    right-=1
                else:
                    left+=1
                
            
        return area

        
            