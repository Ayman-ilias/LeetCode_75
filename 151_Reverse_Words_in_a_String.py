class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        ans=[]
        l=0
        r=len(w)-1
        while l<r:
            w[l],w[r]=w[r],w[l]
            l+=1
            r-=1
        return " ".join(w)
        