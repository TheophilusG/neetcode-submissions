class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        nlen= len(numbers)
        leftindex = 0
        rightindex = nlen-1
        
        while leftindex < rightindex:

            if numbers[leftindex] + numbers[rightindex] == target:
                return [leftindex, rightindex]
            
            elif numbers[leftindex] + numbers[rightindex] < target:
                leftindex+=1
            
            else:
                rightindex-=1
        return []
            



        