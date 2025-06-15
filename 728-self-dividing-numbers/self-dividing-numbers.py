class Solution:
    # Function to find all self-dividing numbers in a given range
    def selfDividingNumbers(self, left, right) :
        ans = []  # List to store self-dividing numbers
        for i in range(left, right+1):  # Iterate through numbers in the range
            if self.helperSelfDividingNumber(i):  # Check if the number is self-dividing
                ans.append(i)  # Add to the result list if it is
        return ans  # Return the final list

    # Helper function to check if a number is self-dividing
    def helperSelfDividingNumber(self, num):
        for i in str(num):  # Convert the number to a string to iterate over its digits
            if i == '0' or num % int(i) != 0:  # If it contains '0' or isn't divisible by its own digit
                return False  # Not a self-dividing number
        return True  # It is a self-dividing number