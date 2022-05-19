class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal)
        if m != n:
            return False
        for i in range(n):
            for j in range(n):
                if s[(i + j) % n] != goal[j]:
                    break
            else:
                return True
        return False


        # else:
        #     for i in range(nums):
        #         a=list2.index(list1[0])
        #         for i in range(ls):
        #             if a==ls:
        #                 a-=ls
        #             if list2[a]!=list1[i]:
        #                 break
        #             a+=1






if __name__ == '__main__':
            s = Solution()
            print(s.rotateString("abcdef","defabc"))