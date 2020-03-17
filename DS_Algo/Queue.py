class MyQueue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        item = self.queue[0]
        del self.queue[0]
        return item

    def peek(self):
        return self.queue[1]

    def total_size(self):
        return len(self.queue)

    def show(self):
        i = 0
        while i < self.total_size():
            print(self.queue[i], end=' ')
            i += 1
        print()


if __name__ == '__main__':
    print("Hello - initialing queue")
    qu = MyQueue()
    qu.enqueue(10)
    qu.enqueue(20)
    qu.enqueue(40)
    qu.enqueue(90)
    qu.enqueue(50)
    print("total size {}".format(qu.total_size()))
    qu.show()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    print("total size {}".format(qu.total_size()))
    qu.show()





