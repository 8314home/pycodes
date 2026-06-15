#input_nums=[-3, 1, 2, 3] expected result = [3, 2, 1, -3] 2 Pointer Method

def reverse(nums):
    start_index = 0
    end_index = len(nums)-1

    while start_index<end_index:
        #keep swapping
        nums[start_index],nums[end_index] = nums[end_index],nums[start_index]
        start_index += 1
        end_index -= 1
        print(nums)
    return nums


input_nums=[-3, 1, 2, 3]
reverse(input_nums)

# Palindrome exercise is_palindrome()

def is_palindrome(word):
    start_index = 0
    end_index = len(word)-1

    while start_index<end_index:
        #check if word[start_index] == word[end_index]
        if word[start_index] != word[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True

input_word = 'radar'
print(f"is_palindrome({input_word}) :  {is_palindrome(input_word)}")

# input_word[::-1] reads from back to front
def is_palindrome2(input_word):
    return True if input_word == input_word[::-1] else False

print(f"is_palindrome2({input_word}) :  {is_palindrome2(input_word)}")


# Integer reverse - Not using string or list - 2 variable
def reverse_integer(n):
    reversed = 0
    remainder = 0
    while n > 0 :
        remainder = n % 10
        reversed = reversed * 10 + remainder
        n = n //10 
        print(reversed)
    return reversed

n = 123450
print(f"reverse_integer => {reverse_integer(n)}")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Single_linked_List:
    def __init__(self):
        self.head = None
        self.sll_size= 0

    def size_of_ll(self):
        return self.sll_size
    
    def traverse(self):
        if self.sll_size == 0:
            print('empty Single LL')
            return 
        else:
            c = self.head
            while c is not None:
                print(f"{str(c.data)} ->",end='')
                c = c.next

    def insert_at_end(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.sll_size += 1
    
    def reverse_in_place(self):

        prev = None 
        curr = self.head
        next = None 

        while curr is not None:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        self.head = prev
        self.traverse()



class Doubly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.dll_size = 0
    
    def size_of_ll(self):
        return self.dll_size
    
    def traverse(self):
        if self.dll_size == 0:
            print('empty doubly LL')
            return 
        else:
            c = self.head
            while c is not None:
                print(f"{str(c.data)} ->",end='')
                c = c.next

    
    def insert_at_end(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.dll_size += 1

    def insert_at_front(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.dll_size += 1

    def middle_node_of_ll(self):
        mid_p = self.head
        end_p = self.head

        while end_p.next is not None and end_p.next.next is not None:
            mid_p = mid_p.next
            end_p = end_p.next.next
        return mid_p.data
    
    def remove_item(self,value):
        # No item 
        if self.head is None:
            print(f"list is empty")
            return
        # 1 item
        if self.head.next is None:
            print(f"list has 1 item, removing")
            self.head= None

        curr = self.head 
        while curr.next is not None:
            if curr.data == value:
                ##delete curr node
                print(f"value found - removing node")
                prev_node = curr.prev
                next_node = curr.next
                prev_node.next = next_node
                next_node.prev = prev_node
                curr.prev = None
                curr.next = None
                self.traverse()
                return
            curr = curr.next
        
        print(f"ITEM NOT FOUND")
        return



if __name__ == '__main__':

    sll = Single_linked_List()
    print(f"sll.size_of_ll - {sll.size_of_ll()}")
    sll.traverse()

    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.insert_at_end(40)

    sll.traverse()
    print("\nreverse_in_place")
    sll.reverse_in_place()



    print(f'\n____DOUBLE LINK LIST_____\n')

    dll = Doubly_linked_list()
    print(f"dll.size_of_ll - {dll.size_of_ll()}")
    dll.traverse()

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_front(40)

    dll.insert_at_end(15)
    dll.insert_at_end(25)
    dll.insert_at_end(35)
    dll.insert_at_front(45)
    dll.insert_at_end(55)

    dll.traverse()

    print(f"\nmiddle_node_of_ll-{dll.middle_node_of_ll()}")

    dll.remove_item(15)





    