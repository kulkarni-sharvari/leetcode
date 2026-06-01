# 146 - LRU Cache - https://leetcode.com/problems/lru-cache/description/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4



################################# Using Queue #################################
############################# Time Limit Exceeded #############################

# From the question constraints: The functions get and put must each run in O(1) average time complexity.
# This execution logic `gets` and `puts` the value in Θ(n)

# to get the in O(1) we should use a Hashmap
# to put a value, used Double linked list for quick access to Most recently used key and least recently used key.

from collections import deque
class LRUCache:


    def __init__(self, capacity: int):
        self.cache = deque()
        self.count = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        for item in self.cache:
            if item["key"] == key:
                value = item["value"]
                self.cache.remove({"key":key, "value": value })
                self.cache.append({"key":key, "value": value })
                return value
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        
        val = self.get(key)
        if val != -1:
            idx = self.cache.index({"key":key, "value": val})
            self.cache[idx] = {"key":key, "value": value}
        else:
            if self.count == self.capacity:
                self.cache.popleft()
                self.count -= 1
            self.cache.append({"key":key, "value": value})
            self.count += 1
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

class ListNode:
    def __init__(self, key=0, val=0, next=None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        node = self.cache.get(key, None)
        if node:
            if node != self.head.next:
                node.prev.next = node.next
                node.next.prev = node.prev

                currentRecent = self.head.next
                self.head.next = node
                node.prev = self.head

                node.next = currentRecent
                currentRecent.prev = node
            
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
        # key already exists.
            node.val = value
            self.get(key)
        # new key
        else:
            addNode = ListNode(key, value)
            # size >= capacity
            if len(self.cache) >= self.capacity:
                leastRecent = self.tail.prev
                self.tail.prev = leastRecent.prev
                leastRecent.prev.next = self.tail

                self.cache.pop(leastRecent.key, None)
            # size < capacity
            if self.head.next == self.tail:
                self.head.next = addNode
                addNode.prev = self.head
                addNode.next = self.tail
                self.tail.prev = addNode

            else:
                currentRecent = self.head.next
                self.head.next = addNode
                addNode.prev = self.head
                addNode.next = currentRecent
                currentRecent.prev = addNode
            self.cache[key] = addNode

       

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)