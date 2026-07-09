class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums) # sort first
        nlen = len(nums)

        triplets = [] 
      

        for i in range(nlen-2):

            l=i+1         # left pointer
            r= nlen-1   # right pointer

            while(l<r):

                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    
                l+=1
                r-=1
                


        unique_list = [list(x) for x in set(tuple(sorted(sublists)) for sublists in triplets)]

        return unique_list 


                
        
      
        