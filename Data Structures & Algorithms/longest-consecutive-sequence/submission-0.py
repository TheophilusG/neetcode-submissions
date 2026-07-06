class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      
        
        conscutive_count = 0
        sorted_nums = sorted(nums)
        seen = []
        is_first = True

        for i in sorted_nums:

            if is_first:
                conscutive_count+=1
                is_first = False
                seen.append(i)
            else:
                if (i - seen[-1]) == abs(1):
                    conscutive_count+=1
                    seen.append(i)
                    
        return conscutive_count
            


        