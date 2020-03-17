class MyStack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def peek(self):
        return self.stack[-1]

    def total_size(self):
        return len(self.stack)

    def show(self):
        i = 1
        while i <= self.total_size():
            print(self.stack[-i],end=' ')
            i += 1
        print()


if __name__ == '__main__':
    print("Hello -- initiating stack")
    st = MyStack()
    st.push(10)
    st.push(30)
    st.push(20)
    st.push(40)
    st.show()
    print("Peeking : {}".format(st.peek()))
    print("Size of stack : {}".format(st.total_size()))
    st.pop()
    st.pop()
    print("Peeking : {}".format(st.peek()))
    print("Size of stack : {}".format(st.total_size()))
    st.show()
