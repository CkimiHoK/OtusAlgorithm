class Node:
    def __init__(self, item, prev_node=None, next_node=None):
        self.item = item
        self.prev_node = prev_node
        self.next_node = next_node


class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item, self.tail, None)  # create new node

        if self.tail is not None:  # fill tail node
            self.tail.next_node = new_node
        self.tail = new_node

        if self.head is None:  # fill head node
            self.head = new_node

    def dequeue(self):
        result = self.head.item if self.head else None

        if self.head is not None:  # move head to next item in deque
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev_node = None

        return result


class MyPriorityQueue:
    def enqueue(self, priority, item):
        pass

    def dequeue(self):
        pass


print("let's go")

n = Node("first")
n_2 = Node("second")
n_3 = Node("third", n, n_2)

print(f'{n_3.item} - {n_3.prev_node.item} - {n_3.next_node.item}')

deque = MyDeque()
deque.enqueue("one")
deque.enqueue("two")
deque.enqueue("three")
deque.enqueue("four")
deque.enqueue("five")
deque.enqueue("one")
deque.enqueue("two")
deque.enqueue("three")
deque.enqueue("four")
deque.enqueue("five")

for _ in range(50):
    item = deque.dequeue()
    print(item)
    if item is None:
        break
