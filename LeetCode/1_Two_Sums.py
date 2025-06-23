# l=[1,2,3,4] target=6 //[1,3]
class Solution():
    def twoSum(self,l,t):
        h={}
        for i,n in enumerate(l):
            diff=t-n
            if diff in h:
                return(h[diff],i)
            h[n]=i


            
