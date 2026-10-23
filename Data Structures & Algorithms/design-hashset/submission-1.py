class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]

        

    def add(self, key: int) -> None:
        index = key % 10 

        if key not in self.buckets[index]:
            self.buckets[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % 10
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
        

    def contains(self, key: int) -> bool:
        index = key % 10
        return  key in self.buckets[index]
          

myHashSet = MyHashSet()

myHashSet.add(1)
myHashSet.add(2)

myHashSet.contains(1) # True
myHashSet.contains(3)  # False

myHashSet.add(2)
myHashSet.contains(2) # True

myHashSet.remove(2)
myHashSet.contains(2)  # False
    

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)