class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False 

        Hash_S, Hash_T = {}, {}

        for i in range(len(s)):

            Hash_S[s[i]] = 1 + Hash_S.get(s[i], 0)
            Hash_T[t[i]] = 1 + Hash_T.get(t[i], 0)
        
        for k in Hash_S:
            if Hash_S[k] != Hash_T.get(k, 0):
                return False 
        
        return True  
        
    



        