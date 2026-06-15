## Queue using stack
## Max element of stack in O(1) time


class stack:
    def __init__(self):
        self.s = []
        self.s_len = 0
        self.max_stack = []

    def size_of_stack(self):
        return self.s_len

    def traverse(self):
        print(f'STACK - stack size - {self.size_of_stack()} ')
        for i in range(self.s_len-1,-1,-1):
            print(f"{self.s[i]}",end=' ')
        print('\n')

    def traverse_max_stack(self):
        print('MAX STACK - ')
        for i in range(self.s_len-1,-1,-1):
            print(f"{self.max_stack[i]}",end=' ')
        print('\n')
        print(f'MAX_STACK_ELEMENT = {self.max_stack[-1] if len(self.max_stack)>0 else None}')
        
    def push(self,data):

        # if stack was empty then just push to max_stack
        # if not empty , compare current top value of max stack with incoming value (data), if greater then insert incoming value , 
        # else another entry of top value of max stack

        self.s.append(data)
        self.s_len +=1

        if len(self.max_stack) == 0:
            self.max_stack.append(data)
        else:
            max_stack_max_val = self.max_stack[-1]
            if data > max_stack_max_val:
                self.max_stack.append(data)
            else:
                self.max_stack.append(max_stack_max_val)

    def peek(self):
        return self.s[-1]
    
    def pop(self):
        if len(self.s) == 0:
            print('No item in stack')
            return None
        
        last_data = self.s[-1]
        del self.s[-1]
        self.s_len -=1
        del self.max_stack[-1]
        return last_data

# Queue using two stack   

class Queue:
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()
    
    def push(self,data):
        self.s1.push(data)

    def pop(self):
        if self.s2.size_of_stack() == 0:
            while self.s1.size_of_stack()!= 0:
                x = self.s1.pop()
                self.s2.push(x)
        pop_data = self.s2.pop()
        return pop_data

    def peek(self):
        if self.s2.size_of_stack() == 0:
            while self.s1.size_of_stack()!= 0:
                x = self.s1.pop()
                self.s2.push(x)
        return self.s2.peek()
    
    def traverse(self):
        print(f's2:')
        self.s2.traverse()
        print(f's1:')
        self.s1.traverse()


    

if __name__ == '__main__':
    stack1 = stack()
    stack1.push(6)
    stack1.push(5)
    stack1.push(8)
    stack1.push(2)
    stack1.push(14)
    stack1.push(11)

    stack1.pop()
    stack1.pop()

    print('-------QUEUE--------')

    q = Queue()

    q.push(10)
    q.push(20)
    q.push(30)
    q.traverse()

    print(f'Next pop operation 1={q.pop()}')
    q.traverse()

    q.push(40)
    q.push(50)
    q.push(60)
    print(f'Next pop operation 2={q.pop()}')
    q.traverse()

    q.push(100)
    q.traverse()

    print(f'Next pop operation 3={q.pop()}')
    q.traverse()

    print(f'Next pop operation 4={q.pop()}')
    q.traverse()

    print(f'Next pop operation 5 ={q.pop()}')
    q.traverse()


