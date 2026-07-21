class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    
        result = {}
        stack = []

        for i in range(len(temperatures)):
            days = 0
            if len(stack) == 0:
                stack.append(temperatures[i])
                result[temperatures[i]] = days

            for j in stack:

                if temperatures[i] < stack[j]:
                    days+=1

                stack.append(temperatures[i])
                result[temperatures[i]] = days
        
        # we have now a dictionary of {temperature:numberofdays} 

        return list(result.values())

            

        