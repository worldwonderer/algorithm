
# @Title: LRU 缓存机制 (LRU Cache)
# @Author: 18015528893
# @Date: 2021-02-28 17:17:13
# @Runtime: 196 ms
# @Memory: 23.4 MB

class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoubleList:

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_first(self):
        if self.head.next == self.tail:
            return
        first = self.head.next
        self.remove(first)
        return first

    def add_last(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
        self.size += 1


class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict()
        self.cache = DoubleList()
        self.capacity = capacity        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.make_recent(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete_key(key)
            self.add_recent(key, value)
            return
        
        if self.capacity == len(self.map):
            self.remove_least_recent()

        self.add_recent(key, value)

    def make_recent(self, key):
        node = self.map[key]
        self.cache.remove(node)
        self.cache.add_last(node)
    
    def add_recent(self, key, val):
        node = Node(key, val)
        self.cache.add_last(node)
        self.map[key] = node

    def delete_key(self, key):
        node = self.map[key]
        self.cache.remove(node)
        del self.map[key]
    
    def remove_least_recent(self):
        node = self.cache.remove_first()
        del self.map[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
