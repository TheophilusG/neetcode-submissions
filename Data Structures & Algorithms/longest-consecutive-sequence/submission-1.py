class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        Nset = set(nums)
        sequence_length = 0
        
        for n in Nset:
            if (n-1) not in Nset:
                length = 0

                while(n+length) in Nset:
                    length+=1
                sequence_length = max(length, sequence_length)

        return sequence_length        
      


        