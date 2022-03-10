class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        nums=[]
        ls=len(bills)
        for i in range(ls):
            if bills[i]==5:
                nums.append(bills[i])
            elif bills[i]==10:
                if 5 in nums:
                    nums.remove(5)
                    nums.append(10)
                else:
                    return False
            else:
                if 5 not in nums:
                    return False
                elif (5 and 10) in nums:
                    nums.remove(5)
                    nums.remove(10)
                elif 5 in nums:
                    if nums.count(5)>=3:
                        nums.remove(5)
                        nums.remove(5)
                        nums.remove(5)
                    else:
                        return False
        return True
if __name__ == '__main__':
            s = Solution()
            print(s.lemonadeChange([5,5,5,10,20]))



