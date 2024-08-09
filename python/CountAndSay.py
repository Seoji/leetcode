# Runtime: 45 ms
# Memory Usage: 16.6 MB

class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"
        for _ in range(n-1):
            count = 0
            previous_char_int = None
            new_rle = ""
            
            for idx, char_int in enumerate(list(rle)):
                if idx > 0:
                    if char_int != previous_char_int:
                        new_rle = new_rle + f"{count}{previous_char_int}"
                        count = 0
                previous_char_int = char_int
                count+=1
            else:
                rle = new_rle + f"{count}{previous_char_int}"
        return rle
                
