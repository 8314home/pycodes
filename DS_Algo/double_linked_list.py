class Node(object):

    def __init__(self,data):
        self.data = data
        self.previousNode = None
        self.nextNode = None


class double_Linked_List(object):

    def __init__(self):
        self.previousNode = None
        self.head = None
        self.total_size = 0

    def insert_at_start(self, data):
        tmpnode = Node(data)
        #print("created a node with value {}".format(data))
        if self.total_size == 0:
            self.head = tmpnode
        else:
            tmpnode.nextNode = self.head
            self.head.previousNode = tmpnode
            self.head = tmpnode
        self.total_size += 1

    def insert_at_end(self,data):
        tmpnode = Node(data)
        #print("created a node with value {}".format(data))
        if self.total_size == 0:
            self.head = tmpnode
        else:
            current_node = self.head
            while current_node.nextNode is not None:
                current_node = current_node.nextNode

            current_node.nextNode = tmpnode
            tmpnode.previousNode = current_node

        self.total_size += 1



    def remove(self, data):
        current_node = self.head
        while current_node.data != data:
            current_node = current_node.nextNode

        if current_node is not None:
            prev_node = current_node.previousNode
            next_node = current_node.nextNode
            prev_node.nextNode = next_node
            next_node.previousNode = prev_node
            print("deleted item {}".format(data))
        else:
            print("did not find element to del")

    def traverse(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.nextNode
        print()


if __name__ == '__main__':
    print("Hello")
    dll = double_Linked_List()
    dll.insert_at_start(10)
    dll.insert_at_start(20)
    dll.insert_at_start(30)
    dll.insert_at_end(50)
    dll.insert_at_end(60)
    dll.traverse()
    dll.remove(10)
    dll.traverse()



