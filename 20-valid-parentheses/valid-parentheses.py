class Solution:
    def isValid(self, s: str) -> bool:
        pairs=["()","[]","{}"]
        while True:
            found_pair=False
            for pair in pairs:
                if pair in s:
                    s=s.replace(pair,"")
                    found_pair=True
            if not found_pair:
                break
        return len(s)==0
        