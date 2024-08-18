# Runtime: 32ms
# Memory: 16.54MB

class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        string = ""
        for ch in s:
            if ch == "[":
                stack += string,
                stack += num,
                num, string = 0, ""
            elif ch == "]":
                pre_num, pre_string = stack.pop(), stack.pop()
                string = pre_string + pre_num * string
            elif ch.isdigit(): 
                # 십진수
                num = num * 10 + int(ch)
            else: 
                string += ch
        return string
