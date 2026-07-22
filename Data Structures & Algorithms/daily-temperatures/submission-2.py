class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        stack = []
        n = len(temperatures)
        result = [] * n

       

        for i in range(n):

            while len(stack) !=0 and temperatures[i] > temperature[stack[-1]]:
               
                current_index = i - stack[-1]
                stack.append(i)
                result[i]= current_index
        
        return result
            
            
            
           


            


            



        

    

            

        