class BSTNode:
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            #if there is no root node
            self.root = BSTNode(data)
        else:
            #if root node exist, then add child at right location
            self._add_child(data, self.root)

    def _add_child(self, data, p_node):
        if data == p_node.data: #duplicate items cannot be added
            return

        if data < p_node.data: #the element is smaller than the root
            if p_node.left: #left child exist
                self._add_child(data, p_node.left)

            else: # left child does not exist
                p_node.left = BSTNode(data, p_node)

        else: #the element is greater than the root
            if p_node.right: #right child exists
                self._add_child(data, p_node.right)

            else: #right child does not exist
                p_node.right = BSTNode(data, p_node)

    def get_max(self):
        if self.root:
            return self._get_right_child(self.root)
        else:
            return None

    def _get_right_child(self, node):
        if node.right:
            return self._get_right_child(node.right)

        return node.data

    def get_min(self):
        if self.root:
            return self._get_left_child(self.root)
        else:
            return None

    def _get_left_child(self, node):
        if node.left:
            return self._get_left_child(node.left)

        return node.data

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)

        print(node.data)

        if node.right:
            self.traverse_in_order(node.right)

    def delete(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)

        else: #the required node to be deleted is found
            if node.left is None and node.right is None:
                print(f"Removing a leaf node with data: {node.data}")
                parent = node.parent

                if parent is not None:
                    if parent.right == node:
                        parent.right = None
                    if parent.left == node:
                        parent.left = None
                else: #if the element we are removing is root
                    self.root = None

                del node

            elif node.left is None and node.right is not None:
                print(f"Removing node having a right child with data: {node.data}")
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

            elif node.left is not None and node.right is None:
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

            else: #when both children are present
                print(f"Removing node having the left child ({node.left.data}) \
                and right child ({node.right.data})")

                predecessor = self.get_predecessor(node.left)
                print("predecessor before: ", predecessor.data)
                predecessor.data, node.data = node.data, predecessor.data
                print("predecessor after: ", predecessor.data)
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)

        return node

    def __str__(self) -> str:
        #print the whole tree in a string format and make it look like a tree

        if self.root is None:
            return "The tree is empty"
        
        self._print_tree(self.root)
        return ""
        
    def _print_tree(self, node, indent="", last="root"):
        if node:
            print(indent, last, node.data)
            indent += "     "
            self._print_tree(node.left, indent, "L:")
            self._print_tree(node.right, indent, "R:")

    def rotate_left(self, node):
        print(f"Rotating to the left on node: {node.data}")

        temp_right = node.right
        t = temp_right.left

        temp_right.left = node
        node.right = t

        if t != None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right

        if temp_parent != None:
            temp_right.parent = temp_parent

        if temp_right.parent.left == node:
            temp_right.parent.left = temp_right

        if temp_right.parent.right == node:
            temp_right.parent.right = temp_right

        if node == self.root:
            self.root = temp_right

    def rotate_right(self, node):

        temp_left = node.left
        t = temp_left.right

        temp_left.right = node
        node.left = t

        if t != None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left

        if temp_parent != None:
            temp_left.parent = temp_parent

        if temp_left.parent.left == node:
            temp_left.parent.left = temp_left

        if temp_left.parent.right == node:
            temp_left.parent.right = temp_left

        if node == self.root:
            self.root = temp_left

        



if __name__ == "__main__":
    BST = BinarySearchTree()
    # BST.insert(12)
    # BST.insert(4)
    # BST.insert(8)
    # BST.insert(55)
    # BST.insert(27)

    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST.insert(data)

    print(f"Max: {BST.get_max()}")
    print(f"Min: {BST.get_min()}")

    BST.traverse_in_order(BST.root)

    BST.delete(12)
    BST.traverse_in_order(BST.root)
    print(BST.root.data)
