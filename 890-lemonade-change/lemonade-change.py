class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic=dict()
        dic={5:0,10:0,20:0}
        for i in range(len(bills)):
            dic[bills[i]]+=1
            if bills[i]>5:
                if bills[i]==10:
                    if dic[5]>0:
                        dic[5]-=1
                    else:
                        return False
                else:
                    if dic[5]>0 and dic[10]>0:
                        dic[5]-=1
                        dic[10]-=1
                    elif dic[5]>2:
                        dic[5]-=3
                    else:
                        return False
        return True


        