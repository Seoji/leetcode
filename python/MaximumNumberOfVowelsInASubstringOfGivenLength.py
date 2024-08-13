class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        substring = None
        for cursor in range(k-1, len(s)):
            if not substring:
                substring = s[0:cursor+1]
            else:
                substring = substring[1:] + s[cursor]
            substr_cnt = len(list((filter(lambda ch: ch in ["a", "e", "i", "o", "u"], substring))))
            result = max(
                result,
                substr_cnt
            )

            if result == k:
                break
        return result
