

class Node:

    def __init__(self, data):
        self.data = data
        self.adj_list = []
        self.visited = False

def bfs(start_node):
    # BFS we start by defining queue and 
    q = [start_node]
    start_node.visited=True

    while q:
        node = q.pop(0)
        print(f'{node.data} -> ', end=' ')

        for neighbour in node.adj_list:
            if neighbour.visited is False:
                neighbour.visited= True
                q.append(neighbour)

def dfs_using_stack(start_node: Node):
    # start with start node and mark it visited
    stack = [start_node]
    start_node.visited=True

    while stack:
        node: Node = stack.pop() # list pop() spits the last item inserted
        print(f'{node.data} ->',end=' ')

        for neighbour in node.adj_list:
            if neighbour.visited is False:
                neighbour.visited = True
                stack.append(neighbour)

def dfs_using_recursion(node):
    if node is None:
        return 
    
    print(f'{node.data} ->', end=' ')
    node.visited = True

    for neighbour in node.adj_list:
        if neighbour.visited is False:
            dfs_using_recursion(neighbour)

def is_valid_tree(root_node):
    print(f'is_valid_tree check:')
    # set of Node , use print([n.data for n in visited_nodes_set])
    visited_nodes_set = set()
    if is_valid(root_node,visited_nodes_set):
        return True
    return False

def is_valid(node, visited_nodes_set: set):
    
    visited_nodes_set.add(node)

    for neighbour in node.adj_list:
        print(f'\nchecking for neighbour = {neighbour.data} current visited_nodes_set= {[n.data for n in visited_nodes_set]}')
        if neighbour in visited_nodes_set:
            print(f'\ncycle found') 
            return False
        if is_valid(neighbour, visited_nodes_set) is False:
            return False
    return True
 



if __name__ == '__main__':

    node_A = Node(data='A')
    node_B = Node(data='B')
    node_C = Node(data='C')
    node_D = Node(data='D')
    node_E = Node(data='E')
    node_F = Node(data='F')
    node_G = Node(data='G')
    node_H = Node(data='H')

    node_A.adj_list.append(node_B)
    node_A.adj_list.append(node_C)
    node_A.adj_list.append(node_D)

    node_C.adj_list.append(node_E)
    node_C.adj_list.append(node_F)

    node_B.adj_list.append(node_G)
    node_G.adj_list.append(node_H)

    print(f'\n BFS Traverse algo')
    bfs(node_A)

    node_A.visited = False
    node_B.visited = False
    node_C.visited = False
    node_D.visited = False
    node_E.visited = False
    node_F.visited = False
    node_G.visited = False
    node_H.visited = False

    print(f'\n DFS using stack Traverse algo')
    dfs_using_stack(node_A)

    node_A.visited = False
    node_B.visited = False
    node_C.visited = False
    node_D.visited = False
    node_E.visited = False
    node_F.visited = False
    node_G.visited = False
    node_H.visited = False

    print(f'\n DFS using recursion algo')
    dfs_using_recursion(node_A)

    print(f'\n\n DETECT CYCLE in a TREE')

    node_K = Node(data='K')
    node_L = Node(data='L')
    node_M = Node(data='M')
    node_N = Node(data='N')
    node_O = Node(data='O')

    node_K.adj_list.append(node_L)
    node_K.adj_list.append(node_M)

    node_M.adj_list.append(node_N)
    node_M.adj_list.append(node_O)

    # make a cycle
    # node_L.adj_list.append(node_O)

    print(f'\n is valid tree ? = {is_valid_tree(node_K)}')







