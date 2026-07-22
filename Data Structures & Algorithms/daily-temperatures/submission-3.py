class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        stack = []
        n = len(temperatures)
        result = [0] * n

       

        for i in range(n):

            while len(stack)!=0 and temperatures[i] > temperatures[stack[-1]]:
                    previous_index = stack.pop()
                    current_index = i - previous_index
                    result[previous_index]= current_index

            stack.append(i)

        return result
            
            
            
           


            


            



        

    

            

        