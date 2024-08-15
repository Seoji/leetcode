# Runtime: 274ms
# Memory: 17.76MB

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dict = dict()
        for word in word1:
            if word not in word1_dict:
                word1_dict[word] = 1
            else:
                word1_dict[word] += 1
        
        word2_dict = dict()
        for word in word2:
            if word not in word2_dict:
                word2_dict[word] = 1
            else:
                word2_dict[word] += 1

        
        if (sorted(list(word1_dict.keys())) == sorted(list(word2_dict.keys()))) and\
            (sorted(list(word1_dict.values())) == sorted(list(word2_dict.values()))):
            return True
        else:
            return False
