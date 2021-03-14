class MyHashMap:
    def __init__(self):
        self.table = [list() for _ in range(1000)]
        self.p = 769

    def hash(self, key):
        return key % self.p

    def put(self, key: int, value: int) -> None:
        cur = self.table[self.hash(key)]
        for i in range(len(cur)):
            if cur[i][0] == key:
                cur[i][1] = value
                return
        cur.append([key, value])

    def get(self, key: int) -> int:
        cur  = self.table[self.hash(key)]
        for i in range(len(cur)):
            if cur[i][0] == key:
                return cur[i][1]
        return -1

    def remove(self, key: int) -> None:
        cur = self.table[self.hash(key)]
        for i in range(len(cur)):
            if cur[i][0] == key:
                cur.pop(i)
                return


if __name__ == '__main__':
    mp = MyHashMap()
    mp.put(1,1)
    mp.put(2, 3)
    mp.get(1)
    print(mp.table)
    print(mp.remove(1))
