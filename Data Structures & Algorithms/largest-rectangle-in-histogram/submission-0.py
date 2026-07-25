class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_stack = [] 
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while heights_stack and heights_stack[-1][1] > h:
                index, height = heights_stack.pop()
                max_area = max(max_area, height*(i-index))
                start = index
            heights_stack.append((start, h))

        
        for i, h in heights_stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area




        
        
        