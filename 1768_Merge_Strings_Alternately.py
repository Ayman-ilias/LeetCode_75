class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        x=len(word1)
        y=len(word2)
        z=0

        while z<x or z<y:
            if z<x:
                ans+=word1[z]
            if z<y:
                ans+=word2[z]
            z+=1
        return ans

        
        