class Solution:
    def hasGroupsSizeX(self, deck: [int]) -> bool:
        if len(deck)==1:return False
        a=[]
        for ch in deck:
            a.append(deck.count(ch))
        a=list(set(a))
        a.sort()
        if len(a)==1:return True
        if len(a)==2 and a[-1]%a[0]==0:return True
        sum=0
        for i in range(2,a[-1]):
            sum=0
            for ch in a:
                if ch%i!=0:
                    break
                else:
                    sum+=1
                if sum==len(a):
                    return True
        return False


if __name__ == '__main__':
            s = Solution()
            print(s.hasGroupsSizeX([0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,3,3,3]))