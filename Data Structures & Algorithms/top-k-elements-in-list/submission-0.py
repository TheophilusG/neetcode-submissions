class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        above_k_ints=[]
        

        for x in nums:
            count[x]= 1 + count.get(x,0)
            if count[x] == k:
                above_k_ints.append(x)
        
        return above_k_ints
            

        

            
            
        
        
        