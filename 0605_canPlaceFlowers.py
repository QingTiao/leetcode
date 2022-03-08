class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        ls=len(flowerbed)
        a=0
        if flowerbed.count(0)<n:return False
        if n==0:return True
        if flowerbed==[0] and n==1:return True
        if flowerbed[0]==flowerbed[1]==0:
            a+=1
            flowerbed[0]=1
        if flowerbed[-1]==flowerbed[-2]==0:
            a+=1
            flowerbed[-1]=1
        for i in range(ls):
            if flowerbed[i]==flowerbed[i-1]==flowerbed[i+1]==0:
                flowerbed[i]=1
                a+=1
        return a>=n



if __name__ == '__main__':
            s = Solution()
            print(s.canPlaceFlowers([0,0,1,0,0,1],2))



