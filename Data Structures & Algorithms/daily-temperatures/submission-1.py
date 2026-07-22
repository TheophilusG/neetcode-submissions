class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        stack = []
        result = [] * len(temperatures)

        
        for i in range(len(temperatures)):
          for j in range(i+1, len(temperatures)-1):
            

            if temperatures[i] > temperatures[j]:
                j+=1

            else:
                stack.append(temperatures[j])
                result[i]= (i - j)
        
        return result
            
            
            
           


            


            



        

    

            

        