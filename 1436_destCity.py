class Solution:
    def destCity(self, paths: [[str]]) -> str:
        cityA=[]
        cityB=[]
        for i in paths:
            cityA.append(i[0])
            cityB.append(i[1])
        for b in cityB:
            if b not in cityA:
                return b



if __name__ == '__main__':
            s = Solution()
            print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))