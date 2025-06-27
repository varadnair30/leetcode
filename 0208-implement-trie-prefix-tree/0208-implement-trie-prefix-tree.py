class Node:

    def __init__(self):
        
        self.links=[None]*26

        self.flag=False

    def containsKey(self,ch):

        return self.links[ord(ch)-97] is not None

    def put(self,ch,node):

        self.links[ord(ch)-97] = node

    def get(self,ch):

        return self.links[ord(ch)-97]

    def setEnd(self):
        self.flag = True

    # Check if the current node
    # marks the end of a word
    def isEnd(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root = Node()

        
        

    def insert(self, word: str) -> None:

        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # Create a new node for
                # the letter if not present
                node.put(ch, Node())
            # Move to the next node
            node = node.get(ch)
        # Mark the end of the word
        node.setEnd()


        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # If a letter is not found,
                # the word is not in the Trie
                return False
            # Move to the next node
            node = node.get(ch)
        # Check if the last node
        # marks the end of a word
        return node.isEnd()
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                # If a letter is not found, there is
                # no word with the given prefix
                return False
            # Move to the next node
            node = node.get(ch)
        # The prefix is found in the Trie
        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)