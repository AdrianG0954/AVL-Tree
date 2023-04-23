# Your name: Adrian Garcia
# Your ID:
# Your section (z82L or z81L):

from BST import BSTNode, BinarySearchTree

class AVLNode(BSTNode):
    def __init__(self, data, parent=None):
        #Inheriting required attributes from BSTNode
        super().__init__(data, parent)

        #Additional "height" attribute for AVLTree Implementation
        self.height = 0

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    #overriding _add_child method from BinarySearchTree Class
    def _add_child(self, data, p_node):
        if data == p_node.data:
            return

        if data < p_node.data:
            if p_node.left: #left child exist
                self._add_child(data, p_node.left)

            else:
                p_node.left = AVLNode(data, p_node)
                #after adding node, update the height parameter
                p_node.height = max(self._calc_height(p_node.left), self._calc_height(p_node.right)) + 1
        else:
            if p_node.right:
                self._add_child(data, p_node.right)
            else:
                p_node.right = AVLNode(data, p_node)
                #after adding node, update the height parameter
                p_node.height = max(self._calc_height(p_node.left), self._calc_height(p_node.right)) + 1

        #after insertion, check for balanced tree violations and fix them
        self._fix_violations(p_node)

    #overriding remove_node method from BinarySearchTree Class
    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:
            if node.left is None and node.right is None:
                #*** if the node is a leaf node ***#
                parent = node.parent

                if parent is not None:
                    if parent.right == node:
                        parent.right = None
                    if parent.left == node:
                        parent.left = None
                else:
                    self.root = None

                del node

                #after deletion, check and fix if the AVL Tree is imbalanced.
                self._fix_violations(parent)

            elif node.left is None and node.right is not None:
                #*** if the node has a right child ***#
                parent = node.parent

                if parent is not None:
                    if parent.right == node:
                        parent.right = node.right
                    if parent.left == node:
                        parent.left = node.right
                else:
                    self.root = node.right

                node.right.parent = parent
                del node

                #after deletion, check and fix if the AVL Tree is imbalanced.
                self._fix_violations(parent)

            elif node.left is not None and node.right is None:
                #*** if the node has a left child ***#
                print(f"Removing node having a left child with data: {node.data}")
                parent = node.parent

                if parent is not None:
                    if parent.right == node:
                        parent.right = node.left
                    if parent.left == node:
                        parent.left = node.left
                else:
                    self.root = node.left

                node.left.parent = parent
                del node

                #after deletion, check and fix if the AVL Tree is imbalanced.
                self._fix_violations(parent)

            else:
                #*** if the node has two children ***#
                predecessor = self.get_predecessor(node.left)
                predecessor.data, node.data = node.data, predecessor.data
                self.remove_node(data, predecessor)

    #Calculate the height of the node.
    def _calc_height(self, node):
        # If the node is None, return -1,
        # otherwise return the default height
        # 20 points
        if node == None:
            return -1
        else:
            return node.height

    #check if the tree is imbalanced.
    def _fix_violations(self, p_node:AVLNode):
        #Starting from the current node, check all the way up till root node
        # i.e. when the parent node becomes None.
        # 20 points
        #Check the height of the node first using _calc_height(node) method and
        #then call the helper function _fix_violations_helper(node) to
        #check the balance factor of the node and make necessary rotations.
        
        if p_node == None:
            return
        p_node.height = max(self._calc_height(p_node.left), self._calc_height(p_node.right)) + 1
        self._fix_violations_helper(p_node)


    def _fix_violations_helper(self, node):
        #Check the balance factor of the node and make necessary rotations.
        # 20 points
        balance_factor = self._calc_balance_factor(node)

        if balance_factor > 1:
            if self._calc_balance_factor(node.left) < 0:
                self._rotate_left(node.left)

            self._rotate_right(node)

        elif balance_factor < -1:
            if self._calc_balance_factor(node.right) > 0:
                self._rotate_right(node.right)

            self._rotate_left(node)


    #Calculate and return the balance factor
    def _calc_balance_factor(self, node):
        #10 points
        if node == None:
            return 0
        else:
            return self._calc_height(node.left) - self._calc_height(node.right)

    def _rotate_left(self,node):

        temp_node = node.right
        t = temp_node.left

        temp_node.left = node
        node.right = t

        if t != None:
            t.parent = node

        temp_node.parent = node.parent

        if node.parent == None:
            self.root = temp_node

        elif node == node.parent.left:
            node.parent.left = temp_node
        else:
            node.parent.right = temp_node

        node.parent = temp_node

        node.height = max(self._calc_height(node.left), self._calc_height(node.right)) + 1
        temp_node.height = max(self._calc_height(temp_node.left), self._calc_height(temp_node.right)) + 1
       
    def _rotate_right(self,node):
        #10 points
        #rotate node to the right
        temp_node = node.left
        t = temp_node.right

        temp_node.right = node
        node.left = t 

        if t != None:
            t.parent = node

        temp_node.parent = node.parent

        if node.parent == None:
            self.root = temp_node

        elif node == node.parent.right:
            node.parent.right = temp_node
        else:
            node.parent.left = temp_node

        node.parent = temp_node

        node.height = max(self._calc_height(node.left), self._calc_height(node.right)) + 1
        temp_node.height = max(self._calc_height(temp_node.left), self._calc_height(temp_node.right)) + 1

    def __str__(self) -> str:
        return super().__str__()
    

if __name__ == '__main__':

    #checking simple tree
    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(6)
    avl.insert(1)
    avl.delete(6)
    #After deleting, the tree should balance itself and make 3 as a root node
    assert(avl.root.data == 3)

    print("Test 1 PASSED!")

    # checking nested rotation
    avl = AVLTree()
    avl.insert(32)
    avl.insert(10)
    avl.insert(1)
    assert (avl.root.data == 10)
    print("Test 2 PASSED!")

    avl.insert(55)
    avl.insert(41)
    avl.insert(19)
    avl.insert(16)
    assert (avl.root.data == 32)
    print("Test 3 PASSED!")

    #Checking if the internal rotation worked.
    #This is the case shown on slides 28-37 in Week12-BalancedBST.pdf lecture slides file
    avl.insert(12)
    assert (avl.root.left.right.data == 16)
    print("Test 4 PASSED!")
