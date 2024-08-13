# Runtime: 141ms
# Memory: 18.04MB
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_list = ["a", "e", "i", "o", "u"]        
        sub_string = s[0:k]
        result = len(list((filter(lambda ch: ch in vowel_list, sub_string))))
        current_cnt = result

        for cursor in range(k, len(s)):
            remove_ch = s[cursor-k]
            add_ch = s[cursor]

            if add_ch in vowel_list:
                current_cnt += 1
            
            if remove_ch in vowel_list:
                current_cnt -= 1
            
            result = max(result, current_cnt)
            if result == k:
                break

        return result




