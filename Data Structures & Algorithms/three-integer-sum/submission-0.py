class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nlen = len(nums)
        triplets = []

        for i in range(nlen):
            for j in range(i+1, nlen):
                for k in range(j+1, nlen):
                    if i!=j!=k and nums[i]+ nums[j] + nums[k] == 0:
                        triplets+=[[nums[i],nums[j],nums[k]]]
                    
        
        return triplets
        