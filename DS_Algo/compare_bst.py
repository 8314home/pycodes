from DS_Algo.BST import BinarySearchTree, Node

class TreeComparator(object):

    def compare_bst(self,node1:Node,node2:Node):

        # leaf node scenario either node from tree1 or tree2 is None,compare to see if other is none as well
        if node1 is None or node2 is None:
            return node1 == node2

        if node1.data != node2.data:
            return False

        return self.compare_bst(node1.left_child,node2.left_child) and self.compare_bst(node1.right_child,node2.right_child)


if __name__ == "__main__":
    print("compare BST")

    bst1 = BinarySearchTree()
    bst2 = BinarySearchTree()

    bst1.insert(10)
    bst1.insert(20)
    bst1.insert(2)
    bst1.insert(8)

    bst2.insert(10)
    bst2.insert(2)
    bst2.insert(8)
    bst2.insert(20)

    tc = TreeComparator()
    if tc.compare_bst(bst1.root,bst2.root):
        print("Two BST are identical")
    else:
        print("Two BST are Different")

