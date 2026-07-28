class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we need to return k such that k is the minimum of h to eat all the bananas
        # k = number of banas/ hour[h]  
            # ith of piles = num of bananas for ith index 
            #piles = [num of bananas , num of bananas]
            
        maxpiles = max(piles)
        k_range = list(range(1, maxpiles+1))
        k_lists = []

        l = 0 
        r = maxpiles

        while l <=r:

            m = (l + r)//2
            k_temp=0

            for bananapile in piles:
                k_temp += bananapile // m

            k_lists.append(k_temp)

            if k_temp < h:
                r = k_temp - 1
            else:
                l = k_temp + 1
        
        return  min(k_lists, key=lambda x: abs(x - h))

