# Runtime: 39 ms
# Memory Usage: 16.7 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(filter(lambda word: word, s.split(" ")))[::-1])
