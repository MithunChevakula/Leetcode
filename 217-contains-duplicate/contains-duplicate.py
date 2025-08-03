class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        n = Counter(arr)
        for key,val in n.items():
            if val>1:
                return True
        return False


    
    


        