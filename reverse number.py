class Solution:
    def reverse(self, x: int):
        if x>=0:
            x=str(x)
            if int(x[::-1])<=(2**31)-1 and int(x[::-1])>=-1*(2**31):
                return(int(x[::-1])) # x[::-! matlab string reverse]
            else:
                return 0
        else:
            x=str(x*-1)
            if int(x[::-1])<=(2**31)-1 and int(x[::-1])>=-1*(2**31):
                return(int(x[::-1])*-1)
            else:
                return 0
            

    
