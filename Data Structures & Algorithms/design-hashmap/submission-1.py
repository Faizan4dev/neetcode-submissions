class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(1000)]


    def put(self, key: int, value: int) -> None:
        index = key % 1000
        for r in range(len(self.buckets[index])):
            if key == self.buckets[index][r][0]:
                self.buckets[index][r][1] = value
                return
            
        self.buckets[index].append([key , value])

    def get(self, key: int) -> int:
        index = key % 1000
        for r in range(len(self.buckets[index])):
            if key == self.buckets[index][r][0]:
               return self.buckets[index][r][1]
        return -1
        
    def remove(self, key: int) -> None:
        index = key % 1000
        for r in range(len(self.buckets[index])):
            if key == self.buckets[index][r][0]:
                self.buckets[index].pop(r)
                return
   

myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))