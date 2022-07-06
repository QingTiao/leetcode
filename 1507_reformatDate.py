class Solution:
    def reformatDate(self, date: str) -> str:
        months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date=date.split()
        year=date[2]
        month=months.index(date[1])+1
        if month<10:
            month='0'+str(month)
        else:
            month=str(month)
        if len(date[0])==3:
            day='0'+date[0][0]
        else:
            day=date[0][0:2]
        return year+'-'+month+'-'+day





if __name__ == '__main__':
            s = Solution()
            print(s.reformatDate(date = "20th Oct 2052"))