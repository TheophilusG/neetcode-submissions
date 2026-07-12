class Solution:
    def maxArea(self, heights: List[int]) -> int:

       
        res = 0 
        l, r = 0, len(heights)-1
        while l <r:
            area= (r-l) * min(heights[l], heights[r])
            #area =  width (r-l) * minimum of the heights[l] or heights[r] 
        
            res = max(res, area)
            #then the max of the all the computed area gets updated 

            if heights[l] < heights[r]: #if the left height is less update the left
                l+=1
            elif heights[l] > heights[r]: # if the right is less update the right
                r-=1
            else:  # if equal update one of them 
                r-=1
        
        return res


        # so the index of heights is the bar
        # we needed to calculate the width (the distance b/n the bars)
        # the vaue of heights array is the height of the bar
        # you need the max area as the solution (max water = max area)


      
        

        