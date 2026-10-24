class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]
        

    def put(self, key: int, value: int) -> None:
        index = key % 10
        for i in range(len(self.buckets[index])):
            if key == self.buckets[index][i][0]:
                self.buckets[index][i][1] = value
                return
            
        self.buckets[index].append([key,value])
        

    def get(self, key: int) -> int:
        index = key % 10
        for i in range(len(self.buckets[index])):
            if key == self.buckets[index][i][0]:
                return self.buckets[index][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        index = key % 10
        for i in range(len(self.buckets[index])):
            if key == self.buckets[index][i][0]:
                self.buckets[index].pop(i)
                return




