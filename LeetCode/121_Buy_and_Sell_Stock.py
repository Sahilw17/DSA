#l[7,1,5,3,6,4] buy stock on day 2 price is 1 and sell it on day 5 price 6 and calculate the profit
class Solution():
    def maxProfit(self,pr):
       l ,r =0,1
       maxp=0
       while(r<len(pr)):
           if(pr[l]<pr[r]):  #7<1 1<5 1<3 1<6
               profit=pr[r]-pr[l] #x profit=4 , 2
            #    maxp=max(maxp,profit) #x 4=(0,4) (4,2)
               if(maxp<profit):
                   maxp=profit
           else:
               l=r #l=1
           r+=1 #r=2 ,3 ,4
       return maxp 

m=Solution()
l=[7,1,5,3,6,4]
print(m.maxProfit(l))
