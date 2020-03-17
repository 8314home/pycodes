# BFS - Queue, vertex visited, enqueue all neighbours -- take out(dequeue) from queue and mark it visited
# and enqueue all it'sneighbours --> continue the process till all noeds are visited ie Queue is empty
# --> In BFS all nodes are processed in a row by row basis (if it is like tree)
#
# Interview q: BFS uses a queue,DFS can be implemented using a stack, but we use recursion, why?
# DFS recursion implementation uses the underlying OS stack using stack memory


class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


class BFS(object):

    def bfs(self, start_node):
        queue = list()
        queue.append(start_node)
        start_node.visited = True

        while queue:
            actual_node = queue.pop(0)
            print("{}".format(actual_node.name))
            for n in actual_node.adjacency_list:
                if not n.visited:
                    n.visited = True
                    queue.append(n)
                    n.predecessor = actual_node


if __name__ == "__main__":
    print("BFS - QUEUE")

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node2.adjacency_list.append(node5)
    node3.adjacency_list.append(node6)

    bfs= BFS()
    bfs.bfs(node1)





