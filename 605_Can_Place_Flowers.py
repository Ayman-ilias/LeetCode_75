class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0]
        l=len(flowerbed)
        c=0

        for i in range(1,l-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                c+=1
        return c>=n
