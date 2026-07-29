class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need to return k such that k is the minimum of h to eat all the bananas
        # k = number of banas/ hour[h]  
            # ith of piles = num of bananas for ith index 
            #piles = [num of bananas , num of bananas]
            
        
        l = 1
        r = max(piles)
        res = r 

        while l <=r:

            k = (l + r)//2
            hours = 0

            for bananapile in piles:
                hours += math.ceil(bananapile / k)


            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res

