class Node:

    def __init__(self,key=None,value=-1, nextt = None) -> None:
        self.key = key
        self.nextt = nextt

class MyHashSet:

    def __init__(self):
        self.myHashMap = [Node() for _ in range(1001)]

    def add(self, key: int) -> None:
        idx = key % 1001

        head = self.myHashMap[idx]
        curr = head

        while curr and curr.nextt:
            if curr.key == key: return
            curr = curr.nextt
        if curr.key == key: return
        curr.nextt = Node(key = key)

    def remove(self, key: int) -> None:
        idx = key % 1001

        head = self.myHashMap[idx]

        curr = head
        prev = None

        while curr:

            if curr.key == key:
                prev.nextt = curr.nextt
                return
            
            prev = curr
            curr = curr.nextt

        return 

    def contains(self, key: int) -> bool:
        idx = key % 1001

        head = self.myHashMap[idx]


        curr = head

        while curr:

            if curr.key == key:
                return True
            curr = curr.nextt

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)