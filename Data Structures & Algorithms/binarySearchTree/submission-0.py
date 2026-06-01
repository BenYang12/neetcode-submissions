class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val)

        #inserting is not neccessarily recursive
        #just traversing, can do with loop

        if not self.root:
            self.root = newNode
            return
        
        curr = self.root

        while True:
            if key > curr.key:
                if not curr.right:
                    curr.right = newNode
                #go right
                curr = curr.right
            elif key < curr.key:
                if not curr.left:
                    curr.left = newNode
                #go left
                curr = curr.left
            else:
                #key we are looking for is equal to curr.key
                #don't insert node
                curr.val = val
                return
        
    
    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val


        return -1
       


    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1 
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def findMin(self,node):
        while node and node.left:
            node = node.left
        return node



    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1 

        while curr and curr.right:
            curr = curr.right
        return curr.val 



    def remove(self, key: int) -> None:
        #Easier way is recursively
        #possible root doesn't change, but if it does change, I need to know about that and make sure BST is consistent
        self.root = self.removeHelper(self.root,key)

    #remove the node with key, return the new root of the subtree after removing that key
    #return tree node, because removing -> augmenting BST
    def removeHelper(self, curr, key) -> TreeNode:
        #base case: looking for node, but end up reaching null
        #what does new subtree look like after we perform deletion on empty tree? -> doesn't exist
        if not curr:
            return None
        
        if key > curr.key:
            #removing from right-> might end up changing right child of curr node
            #return new root of subtree
            curr.right = self.removeHelper(curr.right,key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left,key)
        else:
            #actually handling deletion
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                #swap curr with lowest in right subtree
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key) #does not chain forever
        return curr
       


    def getInorderKeys(self) -> List[int]:
        #DFS Traversal inorder, recursive
        result = []
        self.inorderTraversal(self.root,result)
        return result

    def inorderTraversal(self, root, result):
        #base case 
        if not root:
            return

        #if root is not null
        self.inorderTraversal(root.left,result)
        result.append(root.key)
        self.inorderTraversal(root.right,result)

        
        





