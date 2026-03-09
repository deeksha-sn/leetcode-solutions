class Solution(object):
    def reverse(self, x):
        sign =-1 if x<0 else 1
        x= abs(x)
        rev_str= str(x)[::-1]
        res=int(rev_str)
        return sign * res
        
        