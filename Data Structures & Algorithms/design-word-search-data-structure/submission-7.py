class TrieNode:
    def __init__(self):
        self.children = {} # a: TrieNode, list of children
        self.word = False # designate if end of word

    
# TC: O(n) for addWord(), O(n) for search()
# SC: O(t + n) where n is length of string and t is total number of TrieNodes created in the Trie


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

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # run dfs
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    # normal search
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)

        
        
        
