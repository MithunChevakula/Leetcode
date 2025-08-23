class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        index=0
        for i in range(1,n+1):
            if index<len(target) and i==target[index]:
                ans.append("Push")
                index+=1
            else:
                ans.append("Push")
                ans.append("Pop")
            if index==len(target):
                break
        return ans