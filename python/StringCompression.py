# Runtime: 55 ms
# Memory Usage: 16.66 MB

class Solution:
    def compress(self, chars: List[str]) -> int:
        previous_char = None
        char_count = 0
        result = ""

        for char in chars:
            if previous_char and char == previous_char:
                char_count += 1
            elif not previous_char:
                char_count = 1
                previous_char = char
            elif previous_char and char != previous_char:
                result += previous_char
                if char_count > 1:
                    result += str(char_count)

                char_count = 1
                previous_char = char
        else:
            result += previous_char
            if char_count > 1:
                result += str(char_count)
        
        for idx, char in enumerate(list(result)):
            chars[idx] = char

        return len(list(result))
