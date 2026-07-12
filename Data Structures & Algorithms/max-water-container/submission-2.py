class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # so the index of heights is the bar
        # the vaue of heights array is the height of the bar
        # you need two of the max height bar to get the soultion 
        # max_water volume = max1 = heights[ith] * max2 heights[ith]

        # so then you can also iterate over each and find the two max and return the multiplcation 

        # hlen= len(heights)

        # l = 0
        # r = hlen-1

        # hset = {}

        # for i in range(hlen):
        #     hset[i]= heights[i]
        
        # # now we have the {bar:height} mapped
        # # now sort by values 

        # def getvals(item):
        #     return item[1]
        
        # sorted_hset = sorted(hset.items(), key = getvals, reverse = True)
        

        # key1, val1 = sorted_hset[0]
        # key2, val2 = sorted_hset[1]

        # print(key1)
        # print(val1)

        res = 0 
        l, r = 0, len(heights)-1
        while l <r:
            area= (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                r-=1
        
        return res



       


        

            
            

        

        