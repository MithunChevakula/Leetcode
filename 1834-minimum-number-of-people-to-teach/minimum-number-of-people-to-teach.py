class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # people are 1-indexed in the problem
        langs = [set()] + [set(l) for l in languages]

        need = set()
        for u, v in friendships:
            if langs[u].isdisjoint(langs[v]):
                need.add(u)
                need.add(v)

        if not need:
            return 0

        ans = float('inf')
        # try each language as the one to teach
        for L in range(1, n + 1):
            cnt = sum(1 for person in need if L not in langs[person])
            ans = min(ans, cnt)
        return ans