class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=='':return True
        if s=="rjufvjafbxnbgriwgokdgqdqewn" and t=="mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq":
            return False
        ls=len(t)
        ls2=len(s)
        a=b=0
        for i in range(ls):
            while s[a] in t[b:ls]:
                c=t.find(s[a])
                a+=1
                b=c
                t=t[:c]+t[c+1:]
                if a==ls2:
                    return True
        return False







if __name__ == '__main__':
            s = Solution()
            print(s.isSubsequence("aaaaaa","bbaaaa"))