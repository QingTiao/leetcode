class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name=list(name)
        typed=list(typed)
        ls=len(typed)
        i=0
        j=0
        if len(name)>ls:
            return False
        if name[-1]!=typed[-1]:
            return False
        while j<ls:
            if i>=len(name):
                i=len(name)-1
            if name[i]==typed[j]:
                i+=1
                j+=1
            elif j>0 and typed[j]==typed[j-1]:
                j+=1
            else:
                return False
        if i>=len(name)-1:
            return True
        else:return False

if __name__ == '__main__':
            s = Solution()
            print(s.isLongPressedName("alex","aaleex"))