class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def data(self):
        return self.data


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.total_size = 0

    def insert_at_head(self, new_data): # O(1) complexity for adding elem at start

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

        self.total_size += 1

    def size_of_ll(self):
        return self.total_size

    def last_node_from_list(self):
        if self.total_size > 0:
            current_node = self.head
            while current_node.nextNode is not None:
                current_node = current_node.nextNode
            last_node = current_node
            return last_node
        else:
            return None

    # O(n) time complexity as we need to traverse the list
    def insert_at_end(self, data):
        new_node = Node(data)
        last_node = self.last_node_from_list()
        last_node.nextNode = new_node

    def del_from_start(self):
        current_node = self.head.nextNode
        self.head = current_node
        print("node deleted from start")

    # Remove operation for a single linked list is O(n) time complexity as we need to traverse till the node
    # and we do not
    # have a reference to previous node for that, but for a diuble linked list since we store both
    # previous node & next node , Just updating th reference will be enough, a O(1) operation.

    def remove(self, data):

        if self.head is None:
            return;
        self.total_size = self.total_size - 1

        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.nextNode

        previous_node.nextNode = current_node.nextNode
        print("removed node with data : {}".format(data))

    def print_all(self):

        if self.total_size > 0:
            print("All elements of list:")
            current_node = self.head
            while True:
                print(current_node.data, end=' ')
                if current_node.nextNode is None:
                    print("\n")
                    break
                current_node = current_node.nextNode
        else:
            print("Empty list")

    # O(n) complexity
    def middle_node_ll(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode: # and usd to brk the loop when fastpointer reach end
            slow_pointer = slow_pointer.nextNode
            fast_pointer = fast_pointer.nextNode.nextNode
        return slow_pointer

    def reverse_linked_list(self):
        prev_node = None
        current_node = self.head

        while current_node:
            tmp_node = current_node.nextNode
            current_node.nextNode = prev_node
            prev_node = current_node
            current_node = tmp_node
        self.head = prev_node


if __name__ == "__main__":
    print("Hello world")

    ll = LinkedList()
    ll.insert_at_head(10)
    ll.insert_at_head(20)
    ll.insert_at_head(30)
    ll.insert_at_head(40)
    ll.insert_at_head(50)
    ll.insert_at_head(70)

    ll.insert_at_end(50)

    print(ll.total_size)
    ll.print_all()

    print("last node")
    print(ll.last_node_from_list().data)

    ll.del_from_start()
    ll.remove(40)
    print(ll.total_size)
    ll.print_all()

    ll.insert_at_end(55)
    print(ll.total_size)
    ll.print_all()
    n1 = ll.middle_node_ll()
    print("middle node {}".format(n1.data))

    print("original linked list")
    ll.print_all()
    ll.reverse_linked_list()
    print("After reversing linked list")
    ll.print_all()
