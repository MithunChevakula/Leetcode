class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        count = Counter(words)
        l = []
        for word in words:
            if count[word] == 1:
                l.append(word)
        return l