# Runtime: 101ms
# MemoryUsage: 28.8MB

class Trie:

    def __init__(self):
        self.ch_dict = {}
        
    def __mv(self, word, Op):
        cur = self.ch_dict
        for c in word:
            if c not in cur:
                if Op != "insert":
                    return False
                cur[c] = {}
            cur = cur[c]
            
        if Op == "insert":
            cur['#'] = None
        else:
            return Op == "startsWith" or '#' in cur
    
    def insert(self, word: str) -> None:
        return self.__mv(word, "insert")
        
    def search(self, word: str) -> bool:
        return self.__mv(word, "search")

    def startsWith(self, prefix: str) -> bool:
        return self.__mv(prefix, "startsWith")
