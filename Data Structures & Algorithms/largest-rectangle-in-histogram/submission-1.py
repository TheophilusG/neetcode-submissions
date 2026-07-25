class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #we are storing a pair of index:height
        max_area = 0

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h: #if the stack's top height is > the current height
                index, height = stack.pop()
                max_area = max(max_area, height * (i-index))
                #calcuate the height and pop
        
                start = index #update the start index to the popped one 

            stack.append((start, h)) # adding the updated stack index, and the current height 

        
        for i, h in stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area




        
        
        