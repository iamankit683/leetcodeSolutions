class Solution
    def romanToInt(self, s str)
        value={'I'1,'V'5,'X'10,'L'50,'C'100,'D'500,'M'1000}
        result=0
        prev=0
        for c in s[-1]
            curr=value[c]
            if prevcurr
                result=result-value[c]
            else
                result=result+value[c]
            prev=curr
        return result
            
        