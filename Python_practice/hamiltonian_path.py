node_dict = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F'
}

class HamiltonianPath:

    def __init__(self, adj_matrix):
        self.n = len(adj_matrix)
        self.adj_matrix = adj_matrix
        self.hamil_path = [] 

    def find_hamiltonian_path(self):
        # we place Node A in postition hamil_path:0 
        self.hamil_path.append(0)

        # solve starting from hamil_path:1 (2nd position)
        if self.solve(1):
            self.print_hamiltonian_path()
        else:
            print('hamiltonian_path not found ')
    
    def print_hamiltonian_path(self):
        for i in self.hamil_path:
            print(node_dict[i] , end='-> ')

    def is_valid_path(self,vertex, hamil_position):
        print(f'checking if we can place {node_dict[vertex]} at hamil_position: [{hamil_position}] ')
        # if vertex visited , return False
        if vertex in self.hamil_path:
            print(f'vertex- {node_dict[vertex]} already in hamil_path, NOT VALID for hamil_position: [{hamil_position}]')
            return False

        # 2. Check if there is an edge between the PREVIOUS vertex in path and current vertex
        # hamil_position = current position in hamil_path we are trying to fill with current vertex
        prev_vertex = self.hamil_path[hamil_position - 1]
        if self.adj_matrix[prev_vertex][vertex] == 0:
            print(f'No edge between [{node_dict[prev_vertex]}][{node_dict[vertex]}]')
            return False
        
        # Means there is a valida path between prev_vertex and vertex
        return True

    def solve(self, hamil_position):

        # base case- when all nodes of graph in hamil path
        if hamil_position == self.n: # ie all nodes have been visited
            return True
        print(f'\nsolving for hamil_path position - {hamil_position}')

        for vertex in range(self.n):

            if self.is_valid_path(vertex, hamil_position):
                self.hamil_path.append(vertex)
                # call for next hamil_position
                if self.solve(hamil_position+1):
                    return True
                # RESET, solve(hamil_position+1) could not be solved, BACKTRACK
                print(f'solution for [{vertex}] at [{hamil_position}] Not found, BACKTRACK')
                self.hamil_path.pop()
        # No path found
        return False

if __name__ == '__main__':
    adj_matrix = [[0,1,0,0,0,1],
                  [1,0,1,0,0,0],
                  [0,1,0,0,1,0],
                  [0,0,0,0,1,1],
                  [0,0,1,1,0,1],
                  [1,0,0,1,1,0]]
    hp = HamiltonianPath(adj_matrix=adj_matrix)
    hp.find_hamiltonian_path()

