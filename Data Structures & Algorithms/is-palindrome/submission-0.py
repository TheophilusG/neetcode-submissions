class Solution:
    def isPalindrome(self, s: str) -> bool:

        left_pointer = 0
        slen = len(s)
        right_pointer = slen-1 

        while left_pointer <= right_pointer:
                if s[left_pointer] == s[right_pointer]:
                    left_pointer+=1
                    right_pointer-=1
                else:
                    return False
        return True 



          
        

        