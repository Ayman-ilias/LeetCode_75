class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        w=list(s)
        vowels="aeiouAEIOU"

        while left<right:
            while left<right and vowels.find(w[left])==-1:
                left+=1
            
            while left<right and vowels.find(w[right])==-1:
                right-=1
            
            w[left],w[right]=w[right],w[left]

            left+=1
            right-=1
        return "".join(w)
            
        