class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #ahh the question wasn't asking k number of times repeated but 
        #top k of the most repated elements 
        #so instead of comparing we sort and compare 
        count = {}

        frq_array = [[] for i in range(len(nums)+1)]

        for x in nums:
            count[x]= 1 + count.get(x,0)
            
        for x, c in count.items():
            frq_array[c].append(x)
        
        result = []
        for i in range(len(frq_array) -1, 0, -1):
            for n in frq_array[i]:
                result.append(n)
                if len(result) == k:
                    return result

        

            
            
        
        
        