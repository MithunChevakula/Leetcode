class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        n = len(arr)

    # Create a set to store the unique elements
        st = set()

    # Iterate through each element
        for i in range(n):
            if arr[i] in st:
                return True
            else:
                st.add(arr[i])

    # If no duplicates are found, return false
        return False
    


        