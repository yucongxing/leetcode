from typing import Optional


class Trie:
    def __init__(self):
        self.isend = False
        self.children = [None for _ in range(26)]

    def insert(self, word: str) -> None:
        p = self
        for w in word:
            index = ord(w) - ord('a')
            if not p.children[index]:
                p.children[index] = Trie()
            p = p.children[index]
        p.isend = True
    def searchPrefix(self, prefix: str) -> Optional["Trie"]:
        p = self
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not p.children[index]:
                return None
            p = p.children[index]
        return p

    def search(self, word: str) -> bool:
        p = self.searchPrefix(word)
        return p is not None and p.isend
    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
