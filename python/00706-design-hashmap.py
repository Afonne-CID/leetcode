class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        # Initialize the object with an empty map (implemented as an array of linked lists).
        self.map = [ListNode() for i in range(1000)]

    def hashcode(self, key):
        # Helper method to calculate the hash code for a given key.
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        # Inserts a (key, value) pair into the hash map. If the key already exists, it updates the corresponding value.
        index = self.hashcode(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # Returns the value associated with the specified key or -1 if the key is not found.
        index = self.hashcode(key)
        cur = self.map[index].next
        while cur and cur.key != key:
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        # Removes the key and its corresponding value from the map if it exists.
        index = self.hashcode(key)
        cur = self.map[index]
        while cur.next and cur.next.key != key:
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next
