# DFS - recursion - mark node visited, check list of node in adjacency list of that node, call DFS()
# on each node from adjacency list

class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


class DFS(object):

    def dfs(self, node):

        print("{}".format(node.name))
        node.visited = True

        for n in node.adjacency_list:
            if not n.visited:
                self.dfs(n)


if __name__ == "__main__":

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node5)
    node1.adjacency_list.append(node6)
    node2.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node1.adjacency_list.append(node2)
    node6.adjacency_list.append(node7)

    dfs = DFS()
    dfs.dfs(node1)


