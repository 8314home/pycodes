class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left_child = None
        self.right_child = None


class AVL(object):

    def __init__(self):
        self.root = None

    def calc_height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def calc_balance(self, node):
        if node is None:
            return 0
        else:
            return self.calc_height(node.left_child) - self.calc_height(node.right_child)
    # Here if balance is at most -1 ot +1 then Balanced property is maintained, but any value beyond is unbalanced.
    # For value less than -1 => left heavy subtree - rotate_right
    # For value greater than +1 => right heavy subtree - rotate_left

    def insert(self, data):
        self.root = self.insert_node(data, self.root)
        print("{} inserted".format(data))
        print("current root - {}\n".format(self.root.data))

    def insert_node(self, data, node):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        if data > node.data:
            node.right_child = self.insert_node(data, node.right_child)
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        print("new data node {} added , will look for balancing against node {}".format(data,node.data))
        return self.settle_violation(data, node)

    def settle_violation(self, data, node):
        balance = self.calc_balance(node)

        # case-1 left left heavy - new data added to left of nodes's left child
        if balance > 1 and data < node.left_child.data:
            print("case-1 left left heavy for node {} - rotate right for node".format(node.data))
            return self.rotate_right(node) # returning root for the subtree where node is root after rotation
        # case-2 right right heavy - new data added to right of nodes's right child
        if balance < -1 and data > node.right_child.data:
            print("case-2 right right heavy for node {} - rotate left for node".format(node.data))
            return self.rotate_left(node)
        if balance > 1 and data > node.left_child.data:
            print("case -3 Two rotations needed left-right heavy")
            print("rotate left for {}".format(node.left_child.data))
            node.left_child = self.rotate_left(node.left_child)
            print("rotate right for {}".format(node.data))
            return self.rotate_right(node)
        if balance < -1 and data < node.left_child.data:
            print("case-4 Two rotations needed right-left heavy")
            print("rotate right for {}".format(node.right_child.data))
            node.right_child = self.rotate_right(node.right_child)
            print("rotate left for {}".format(node.data))
            return self.rotate_left(node)

        return node  # final return statement is for a node with valid balance = 1,0,-1

    def rotate_right(self, node):

        temp_left_child = node.left_child
        t = temp_left_child.right_child

        temp_left_child.right_child = node
        node.left_child = t

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_left_child.height = max(self.calc_height(temp_left_child.left_child), self.calc_height(temp_left_child.right_child)) + 1

        return temp_left_child  # return new root for the node passed

    def rotate_left(self, node):

        temp_right_child = node.right_child
        t = temp_right_child.left_child

        temp_right_child.left_child = node
        node.right_child = t

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_right_child.height = max(self.calc_height(temp_right_child.left_child), self.calc_height(temp_right_child.right_child)) + 1

        return temp_right_child  # return new root for the node passed

    def remove(self, data):
        print("removal for node with data - {}".format(data))
        if self.root:
            self.root = self.remove_node(data, self.root)
        else:
            print("no root present")

    def remove_node(self, data, node):

        if node is None:
            return node

        if data < node.data:
            node.left_child = self.settle_violation(data, self.remove_node(data, node.left_child))
            node.height = max( self.calc_height(node.left_child) , self.calc_height(node.right_child) ) + 1
        elif data > node.data:
            #node.right_child = self.remove_node(data, node.right_child)
            node.right_child = self.settle_violation(data, self.remove_node(data, node.right_child))
            node.height = max( self.calc_height(node.left_child) , self.calc_height(node.right_child) ) + 1
        else:
            if node.left_child is None and node.right_child is None:
                print("removing leaf node")
                del node
                return None
            if node.left_child is None:
                temp_node = node.right_child
                print("removing node with right child only")
                del node
                return temp_node
            if node.right_child is None:
                temp_node = node.left_child
                print("removing node with left child only")
                del node
                return temp_node
            if node.left_child and node.right_child:
                left_subtree_highest_node = self.get_predecessor(node)
                node.data = left_subtree_highest_node.data
                node.left_child = self.remove_node(left_subtree_highest_node.data,node.left_child)
                print("removing node with right & left child")

        return self.settle_violation(data,node)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        else:
            return node

    def traverse(self):
        if self.root:
            self.traverse_node(self.root)
            print("\n")
        else:
            print("No root node")

    def traverse_node(self, node):
        if node.left_child:
            print("\nnode {} has left child {} ".format(node.data,node.left_child.data))
            self.traverse_node(node.left_child)
        print("{}".format(node.data),end=' ')
        if node.right_child:
            print("\nnode {} has right child {} ".format(node.data,node.right_child.data))
            self.traverse_node(node.right_child)


if __name__ == '__main__':
    avl = AVL()
    avl.insert(45)
    avl.insert(35)
    avl.insert(25)
    avl.traverse()
    avl.insert(15)
    avl.traverse()
    avl.insert(10)
    avl.traverse()
    avl.insert(5)
    avl.traverse()
    avl.insert(75)
    avl.insert(85)
    avl.traverse()
    avl.insert(65)
    avl.traverse()

    avl.remove(85)
    avl.remove(75)
    avl.remove(65)
    avl.traverse()

