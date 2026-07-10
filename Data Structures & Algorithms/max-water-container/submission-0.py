class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # so the index of heights is the bar
        # the vaue of heights array is the height of the bar
        # you need two of the max height bar to get the soultion 
        # max_water volume = max1 = heights[ith] * max2 heights[ith]

        # so then you can also iterate over each and find the two max and return the multiplcation 

        hlen= len(heights)

        l = 0
        r = hlen-1

        hset = {}

        for i in range(hlen):
            hset[i]= heights[i]
        
        # now we have the {bar:height} mapped
        # now sort by values 

        def getvals(item):
            return item[1]
        
        sorted_hset = sorted(hset.items(), key = getvals)
        

        key1, val1 = sorted_hset[0]
        key2, val2 = sorted_hset[1]

        return val1*val2



       


        

            
            

        

        