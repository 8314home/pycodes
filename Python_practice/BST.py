class Node:

    def __init__(self,data, parent=None):
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = parent

class BST:

    def __init__(self):
        self.root = None

    def insert_in_BST(self,data):
        if self.root:
            return self.insert_node(data, self.root) 
        self.root = Node(data)

    def insert_node(self,data, node):
        if data < node.data:
            if node.left:
                return self.insert_node(data,node.left)
            else:
                node.left = Node(data,parent = node)
        
        if data > node.data:
            if node.right:
                return self.insert_node(data,node.right)
            else:
                node.right = Node(data,parent = node)

    def min_value_of_bst(self):
        if self.root:
            return self.get_min_node(self.root)

    def get_min_node(self, node):
        if node.left:
            return self.get_min_node(node.left)
        return node
    
    def max_value_of_bst(self):
        if self.root:
            return self.get_max_node(self.root)

    def get_max_node(self, node):
        if node.right:
            return self.get_max_node(node.right)
        return node
    
    def traverse(self):
        if self.root:
            return self.inorder_traversal(self.root)

    def inorder_traversal(self,node):
        if node.left:
            self.inorder_traversal(node.left)
        print(f'{node.data} ->', end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def removal_of_node_from_bst(self,data):
        if self.root:
            self.remove_node(self.root, data)

    def search_node(self,node,data):
        if node is None:
            print(f'{data} not present in tree')
            return None
        if data < node.data:
            return self.search_node(node.left, data)
        elif node.data < data:
            return self.search_node(node.right, data) 
        else:
            return node

    def remove_node(self,node,data):
        # Search for node position where node.data = data
        node_present_in_tree = self.search_node(node, data)
        if node_present_in_tree is None:
            return None
        
        print(f'Node with {data} present in tree, will be removed')
        # 3 cases - leaf node, node with a left or right child, node with both child
        # case-1 LEAF node - no left child, no right child
        parent_of_node_present_in_tree = node_present_in_tree.parent

        if node_present_in_tree.left is None and node_present_in_tree.right is None:
            print(f'node {data} is a leaf node')
            # is the node left or right child of parent ?
            if parent_of_node_present_in_tree is not None and parent_of_node_present_in_tree.left == node_present_in_tree:
                parent_of_node_present_in_tree.left  = None 
            if parent_of_node_present_in_tree is not None and parent_of_node_present_in_tree.right == node_present_in_tree:
                parent_of_node_present_in_tree.right = None 

            if parent_of_node_present_in_tree is None: # ie the current node which has o left or right child is a ROOT node
                self.root = None
            del node_present_in_tree

        # case-2 Node with a left child 
        elif node_present_in_tree.left is not None and node_present_in_tree.right is None:
            print(f'case-2 Node with a left child')

            if parent_of_node_present_in_tree is not None:
                if parent_of_node_present_in_tree.left == node_present_in_tree:
                    # set parent of that left child to parent_of_node_present_in_tree
                    # set node left child to  left child of parent 
                    parent_of_node_present_in_tree.left = node_present_in_tree.left

                if parent_of_node_present_in_tree.right == node_present_in_tree:
                    # set parent of that right child to parent_of_node_present_in_tree
                    # set node right child to  left child of parent 
                    parent_of_node_present_in_tree.right = node_present_in_tree.left
                node_present_in_tree.left.parent = parent_of_node_present_in_tree
            
            if parent_of_node_present_in_tree is None: # ie an original root node with a left or right child only
                self.root = node_present_in_tree.left
            del node_present_in_tree

        # case-3 Node with a right child 
        elif node_present_in_tree.left is None and node_present_in_tree.right is not None:
            print(f'case-3 Node with a right child')

            if parent_of_node_present_in_tree is not None:
                if parent_of_node_present_in_tree.left == node_present_in_tree:
                    parent_of_node_present_in_tree.left = node_present_in_tree.left

                if parent_of_node_present_in_tree.right == node_present_in_tree:
                    parent_of_node_present_in_tree.right = node_present_in_tree.right

                node_present_in_tree.right.parent = parent_of_node_present_in_tree
            
            if parent_of_node_present_in_tree is None: # ie an original root node with a left or right child only
                self.root = node_present_in_tree.right
            del node_present_in_tree

        # case-4 Node with both child
        # Search predecessor of Node with both child
        # Swap predecessor with Node
        # Trigger remove_node() for Node - it will use 
        else:
            print(f'node {data} is a TWO leaf node')
            predecessor_of_node_present_in_tree = self.get_max_node(node_present_in_tree.left)

            tmp = node_present_in_tree.data 
            node_present_in_tree.data = predecessor_of_node_present_in_tree.data
            predecessor_of_node_present_in_tree.data = tmp

            self.remove_node(predecessor_of_node_present_in_tree,data)

    def height_of_tree(self,node, height):
        if node is None:
            return height
        left_side_height = self.height_of_tree(node.left,height + 1 if node.left else height)
        right_side_height = self.height_of_tree(node.right, height + 1 if node.right else height)
        return max(left_side_height,right_side_height)



def compare_bst(node1,node2):

    # check topology - if any of the node is None , (node1 is None and node2 is None) returns True 
    if (node1 is None and node2 is None) or (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
        return node1 == node2
    # check data
    if node1.data != node2.data:
        return False 
    return compare_bst(node1.left, node2.left) and compare_bst(node1.right,node2.right)
    
if __name__ == '__main__':

    bst = BST()

    bst.insert_in_BST(15)
    bst.insert_in_BST(10)
    bst.insert_in_BST(25)
    bst.insert_in_BST(20)
    bst.insert_in_BST(5)
    bst.insert_in_BST(30)

    bst.traverse()

    min_value_of_bst_node = bst.min_value_of_bst()
    max_value_of_bst_node = bst.max_value_of_bst()
    print(f"\n bst.min_value_of_bst - {min_value_of_bst_node.data}")
    print(f"\n bst.max_value_of_bst - {max_value_of_bst_node.data}")

    bst.removal_of_node_from_bst(25)
    bst.traverse()

    bst.removal_of_node_from_bst(10)
    bst.traverse()

    bst2 = BST()
    bst2.insert_in_BST(15)
    bst2.insert_in_BST(10)
    bst2.insert_in_BST(25)
    bst2.insert_in_BST(20)
    bst2.insert_in_BST(5)
    bst2.insert_in_BST(30)
    bst2.removal_of_node_from_bst(25)
    #bst2.removal_of_node_from_bst(10)

    print(f'\nCompare Tree \n')
    bst.traverse()
    print(f'\n')
    bst2.traverse()

    compare_bst_flag = compare_bst(bst.root, bst2.root)
    print(f'\n compare_bst_flag = {compare_bst_flag}')

    print(f'\n height of tree - bst2 => {bst2.height_of_tree(bst2.root, 0)}')



