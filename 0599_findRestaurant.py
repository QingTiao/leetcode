class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        res=[]
        ls1=len(list1)
        ls2=len(list2)
        a=ls1+ls2
        for i in range(ls1):
            for j in range(ls2):
                if list1[i]==list2[j] and i+j<a:
                    if res!=[]:
                        res.pop()
                    res.append(list1[i])
                    a=i+j
                elif list1[i]==list2[j] and i+j==a:
                    res.append(list1[i])
                    a=i+j
        return res



if __name__ == '__main__':
            s = Solution()
            print(s.findRestaurant(list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"],list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))

