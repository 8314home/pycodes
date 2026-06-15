# Cut a Rod of given length say L = 5m.so that we can get max profile by selling pieces
# each portion of rod cutting has different individual prices prices_list

class RodCuttingProblem:

    def __init__(self,rod_length,price_list):
        self.rod_length = rod_length
        self.price_list = price_list
        self.S = [[0] * (rod_length+1) for _ in range(len(price_list))]

    def solve(self):

        for first_i_pieces in range(1,len(self.price_list)) : # row index including last item
            for rod_length_considered in range(1,self.rod_length+1): # column index including last item

                if first_i_pieces <= rod_length_considered: # first_i_pieces=i , rod_length_considered=j
                    #valid check if we can cut
                    self.S[first_i_pieces][rod_length_considered] = max ( 
                        self.S[first_i_pieces-1][rod_length_considered],  # do not make the cut
                          self.price_list[first_i_pieces] + self.S[first_i_pieces][rod_length_considered - first_i_pieces] # make the cut of piece length , see if can be cut again of same piece length
                          )
                    # Multiple Cuts: By changing self.S[first_i_pieces-1] to self.S[first_i_pieces] 
                    # in the "make the cut" logic, you allowed the algorithm to say: "I used a 2m piece, now let me look at the same row to see if I can use another 2m piece."

                else: # ie first_i_pieces > rod_length_considered
                    # first_i_pieces length more than remaing length of rod
                    # keep profit of first_i_pieces-1 pieces 
                    self.S[first_i_pieces][rod_length_considered] = self.S[first_i_pieces-1][rod_length_considered]
        
        # Solved Now print 2 D matrix
        for first_i_pieces in range(len(self.price_list)) : # row index
            for rod_length_considered in range(self.rod_length+1): # column index
                print(f'{self.S[first_i_pieces][rod_length_considered]}', end=' ')
            print('\n')

        # which pieces 
        row_index = len(self.price_list)-1 # first i pieces
        column_index = self.rod_length # rod length
        while column_index>0:
            if self.S[row_index-1][column_index] == self.S[row_index][column_index]:
                row_index = row_index - 1
            else:
                print(f'cut rod of piece = {row_index}m')
                column_index = column_index - row_index # rod length - piece length

        return self.S[len(self.price_list) - 1][self.rod_length]





if __name__=='__main__':
    price_list = [0,2,5,7,3,9]
    N = 5 
    problem = RodCuttingProblem(N, price_list)
    problem.solve()

