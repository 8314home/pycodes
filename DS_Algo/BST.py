class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
# All operation will take O(log n) complexity if Tree is BALANCED - if unbalanced will take O(n) complexity
# to avoid this we use AVL tree or Red Black tree

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_node(self.root,data)

    def _insert_node(self, node,data):
        if node.data > data:
            if node.left_child:
                self._insert_node(node.left_child, data)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self._insert_node(node.right_child, data)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if self.root:
            return self._get_min_node(self.root)

    def _get_min_node(self, node):
        if node.left_child:
            return self._get_min_node(node.left_child)
        else:
            return node.data

    def get_max_value(self):
        if self.root:
            return self._get_max_node(self.root)

    def _get_max_node(self, node):
        if node.right_child:
            return self._get_max_node(node.right_child)
        else:
            return node.data

# Traverse is O(n) complexity
    def traverse(self):
        if self.root:
            print("In order traversal")
            self._traverse_in_order(self.root)
            print("\nPRE order traversal")
            self._traverse_pre_order(self.root)
        else:
            print("No root node")

    def _traverse_in_order(self,node):
        if node.left_child:
            self._traverse_in_order(node.left_child)
        print(node.data, end=' ')
        if node.right_child:
            self._traverse_in_order(node.right_child)

    def _traverse_pre_order(self,node):
        print(node.data, end=' ')
        if node.left_child:
            self._traverse_in_order(node.left_child)
        if node.right_child:
            self._traverse_in_order(node.right_child)

    def _remove_node(self, data, node):

        print("comparing {} and node - {}".format(data, node.data))
        if not node:
            return None

        if data < node.data:
            node.left_child = self._remove_node(data,node.left_child)
        elif data > node.data:
            node.right_child = self._remove_node(data,node.right_child)
        else:
            print("found node with value {}".format(data))
            if not node.left_child and not node.right_child:
                print("a leaf node")
                del node
                return None

            if not node.left_child:
                print("node with only right child")
                temp = node.right_child
                print("deleted node with data {}".format(node.data))
                del node
                return temp
            elif not node.right_child:
                print("node with only left child")
                temp = node.left_child
                print("deleted node with data {}".format(node.data))
                del node
                return temp
            else:
                tempnode = self._get_predecessor(node.left_child)
                node.data = tempnode.data # overwrite/swap with node value with highest value of left sub tree
                node.left_child = self._remove_node(tempnode.data, node.left_child)
        return node   # ---> needed for returning the root node finally

    def _get_predecessor(self, node):
        if node.right_child:
            return self._get_predecessor(node.right_child)
        return node

    def remove(self, data):
        if self.root:
            self.root = self._remove_node(data, self.root)


if __name__ == '__main__':
    print("Hello - BST")
    bst = BinarySearchTree()
    bst.insert(40)
    bst.insert(20)
    bst.insert(15)
    bst.insert(35)
    bst.insert(70)
    bst.insert(45)
    bst.insert(60)
    bst.insert(65)
    bst.insert(67)
    bst.insert(100)
    bst.insert(55)

    bst.traverse()
    print("\n----------------")
    print("Max value : {}".format(bst.get_max_value()))
    print("Min value : {}".format(bst.get_min_value()))
    print("----------------")

    bst.remove(65)
    print("\n----------------")
    bst.traverse()
    print("\n----------------")

    bst.remove(40)
    print("\n----------------")
    bst.traverse()
    print("\n----------------")







