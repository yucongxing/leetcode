class MyHashSet:

    def __init__(self):
        self.HashSet = [list() for _ in range(10 ** 4)]
        self.p = 9973

    def add(self, key: int) -> None:
        for i in range(len(self.HashSet[key % self.p])):
            if self.HashSet[key % self.p][i] == key:
                return
        self.HashSet[key % self.p].append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.HashSet[key % self.p])):
            if self.HashSet[key % self.p][i] == key:
                self.HashSet[key % self.p].pop(i)
                return

    def contains(self, key: int) -> bool:
        for i in range(len(self.HashSet[key % self.p])):
            if self.HashSet[key % self.p][i] == key:
                return True
        return False


if __name__ == '__main__':
    hs = MyHashSet()
    print(hs.add(1))
