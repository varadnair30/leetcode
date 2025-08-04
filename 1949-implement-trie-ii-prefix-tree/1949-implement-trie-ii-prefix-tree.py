class Node:

    def __init__(self):
        self.links=[None]*26
        self.cntEndWith=0
        self.cntPrefix=0

    def containsKey(self,ch):

        return self.links[ord(ch)-97] is not None

    def get(self,ch):

        return self.links[ord(ch)-97]

    def put(self,ch,node):
        

        self.links[ord(ch)-97] = node

    def increaseEnd(self):

        self.cntEndWith+=1

    def increasePrefix(self):

        self.cntPrefix+=1

    def deleteEnd(self):

        self.cntEndWith-=1

    def deletePrefix(self):

        self.cntPrefix-=1

    def getEnd(self):
        return self.cntEndWith

    def getPrefix(self):
        return self.cntPrefix


class Trie:

    def __init__(self):

        

        self.root=Node()
        
    


    def insert(self, word: str) -> None:

        node=self.root
        for ch in word:

            if not node.containsKey(ch):
                node.put(ch,Node())

            node=node.get(ch)

            node.increasePrefix()

        node.increaseEnd()

        

        

    def countWordsEqualTo(self, word: str) -> int:

        node=self.root

        for ch in word:

            if node.containsKey(ch):

                node=node.get(ch)

            else:

                return 0
        return node.getEnd()

        

    def countWordsStartingWith(self, prefix: str) -> int:

        node=self.root

        for ch in prefix:

            if node.containsKey(ch):

                node=node.get(ch)

            else:

                return 0
        return node.getPrefix()


        
        

    def erase(self, word: str) -> None:


        node=self.root

        for ch in word:

            if node.containsKey(ch):

                node=node.get(ch)

                node.deletePrefix()

            else:

                return
        return node.deleteEnd()
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)