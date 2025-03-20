class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lp=0
        lt=0

        while lp < len(s) and lt < len(t):
            if s[lp]==t[lt]:
                lp+=1
            lt+=1
        
        return lp==len(s)

       
            
        