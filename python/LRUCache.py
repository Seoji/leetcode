# Runtime: 591ms
# Memory Usage: 77.3MB

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_node_dict = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.__join(self.head, self.tail)
    
    def get(self, key):
        if key not in self.cache_node_dict:
            return -1
        
        node = self.cache_node_dict[key]
        self.__remove(node)
        self.__move_to_head(node)
        
        return node.value
    
    
    def put(self, key, value):
        if key in self.cache_node_dict:
            node = self.cache_node_dict[key]
            self.__remove(node)
            del self.cache_node_dict[node.key]
        
        if len(self.cache_node_dict.keys()) == self.capacity:
            node = self.tail.prev
            self.__remove(node)
            del self.cache_node_dict[node.key]
        
        new_node = Node(key, value)
        self.cache_node_dict[key] = new_node
        self.__move_to_head(new_node)
    
    def __move_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def __join(self, node1, node2):
        node1.next = node2
        node2.prev = node1
        
    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

