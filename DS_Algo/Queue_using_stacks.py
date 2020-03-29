from DS_Algo.Stack import MyStack

class Queue(object):

    def __init__(self):
        self.enq_stack = MyStack()
        self.dq_stack = MyStack()

    def enque(self,data):
        self.enq_stack.push(data)
        print("added {} in queue ".format(data))

    def dequeue(self):

        if self.dq_stack.total_size == 0 and self.dq_stack.total_size == 0:
            raise Exception("Queue does not have any element")

        if self.dq_stack.total_size() == 0:
            while not self.enq_stack.is_empty():
                item = self.enq_stack.pop()
                self.dq_stack.push(item)
            print("moved items from Enqueue stack to  Dequeue stack")
            val = self.dq_stack.pop()
            print("removed {} in queue ".format(val))
            return
        val_2 = self.dq_stack.pop()
        print("removed {} in queue ".format(val_2))
        return

if __name__ == "__main__":

    my_queue = Queue()
    my_queue.enque(10)
    my_queue.enque(20)
    my_queue.enque(30)
    my_queue.enque(40)
    print("stack enqueue: {} stack dqueue: {}".format(my_queue.enq_stack.total_size(), my_queue.dq_stack.total_size()))
    my_queue.dequeue()
    my_queue.enque(50)
    my_queue.enque(60)
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    print("stack enqueue: {} stack dqueue: {}".format(my_queue.enq_stack.total_size(), my_queue.dq_stack.total_size()))
    my_queue.dequeue()
    my_queue.enque(200)
    my_queue.enque(300)
    print("stack enqueue: {} stack dqueue: {}".format(my_queue.enq_stack.total_size(), my_queue.dq_stack.total_size()))







