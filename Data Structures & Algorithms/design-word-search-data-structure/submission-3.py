class TrieNode:
    def __init__(self):
        self.children = {} #char: TrieNode
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True


        

    def search(self, word: str) -> bool:
        def dfs(j,root): #j is index, root is node
            cur = root


            for i in range(j, len(word)):
                c = word[i] #c could be any character from a-z, it could also be a . character
                if c == ".":
                    #".ab"
                    #could potentially go down 26 paths
                    #Recursion
                    for child in cur.children.values():
                        if dfs(i + 1,child): #remaining portion of word we're trying to match, current node we r at
                            return True
                    return False
                else:
                    #easy
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)
            
