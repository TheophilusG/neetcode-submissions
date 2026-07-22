class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        stack = []
        n = len(temperatures)
        result = [0] * n #initializing array with length temp array
                         # allocating memory equal to the len of temp


        for i in range(n):
                            #the temp[-1] makes sure to check if there is any past appended temp's index that is less than the current one 
                            #and we go back till it is empty 
            while len(stack)!=0 and temperatures[i] > temperatures[stack[-1]]:
                    previous_index = stack.pop() #when you pop you delete it as well
                    current_distance = i - previous_index
                    result[previous_index] = current_distance
            
            stack.append(i)
            #this allows us to add the index of the first one 
            #first run stack is empty and we add 
            #the first index of the 1st temperature 
        return result


            
            
            
           


            


            



        

    

            

        