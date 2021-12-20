# Max value in stack problem - get max value from stack in O(1) complexity
# can use memory
# problem is if we take out evey item from stack we will end up O(n) complexity time
# soln is to create another stack of size n and insert last max item in that


class Stack(object):

    def __init__(self):
        self.stack = list()
        self.max_stack = list()

    def push(self,data):

        self.stack.append(data)
        print("data inserted {}".format(data))
        if len(self.stack) == 1: # 1st element
            self.stack.append(data)
            self.max_stack.append(data)
            return

        max_stack_top_stack = self.max_stack[-1]
        if data > max_stack_top_stack:
            self.max_stack.append(data)
        else:
            self.max_stack.append(max_stack_top_stack)

        return

    def pop(self):
        self.max_stack.pop() # pop() method of list
        return self.stack.pop()

    def max_element(self):
        return self.max_stack.pop()


if __name__ == "__main__":

    stk = Stack()
    stk.push(10)
    stk.push(11)
    stk.push(1)
    stk.push(1000)
    stk.push(12)
    print("Max element from stack")
    print(stk.max_element())
    print(stk.max_stack)



