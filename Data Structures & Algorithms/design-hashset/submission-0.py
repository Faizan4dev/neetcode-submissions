class MyHashSet:

    def __init__(self):
        self.nums = [False] * 1000001

        

    def add(self, key: int) -> None:
        self.nums[key] = True
        

    def remove(self, key: int) -> None:
        self.nums[key] = False
        

    def contains(self, key: int) -> bool:
        return self.nums[key] 

myHashSet = MyHashSet()

myHashSet.add(1)
myHashSet.add(2)

print(myHashSet.contains(1))  # True
print(myHashSet.contains(3))  # False

myHashSet.add(2)
print(myHashSet.contains(2))  # True

myHashSet.remove(2)
print(myHashSet.contains(2))  # False
    

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)