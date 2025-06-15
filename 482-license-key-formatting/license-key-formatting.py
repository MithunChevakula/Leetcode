class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove any dashes and convert all characters to uppercase
        s = s.replace("-", "").upper()

        # Calculate the length of the first group
        first_group_len = len(s) % k

        # Initialize the reformatted license key with the first group
        reformatted = s[:first_group_len]

        # Iterate over the remaining groups and add them to the reformatted license key
        for i in range(first_group_len, len(s), k):
            if reformatted:
                reformatted += "-"
            reformatted += s[i:i+k]

        return reformatted