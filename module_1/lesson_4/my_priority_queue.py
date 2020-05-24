class Node:  # Node element for my deque
    def __init__(self, item, prev_node=None, next_node=None):
        self.item = item
        self.prev_node = prev_node
        self.next_node = next_node


class MyDeque:  # mu own deque structure
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


class PriorityItem:  # link priority with internal deque
    def __init__(self, priority, deque):
        self.priority = priority
        self.deque = deque


class MyPriorityQueue:
    def __init__(self):
        self.__priority_arr = []  # array of PriorityItem elements

    def enqueue(self, priority, item):
        priority_index, is_new = self.__find_priority_index(priority)  # we need to know: is priority item exists ?

        if is_new:  # add new priority type with internal deque
            new_deque = MyDeque()
            new_deque.enqueue(item)
            self.__priority_arr.insert(priority_index, PriorityItem(priority, new_deque))
        else:
            self.__priority_arr[priority_index].deque.enqueue(item)

    def dequeue(self):
        result = None
        while result is None:
            if self.__priority_arr.__len__() <= 0:
                break
            result = self.__priority_arr[0].deque.dequeue()  # get first element
            if result is None:  # delete empty priorities
                self.__priority_arr.pop(0)
        return result

    def __find_priority_index(self, priority):
        return self.__binary_search(priority, 0, self.__priority_arr.__len__() - 1)

    def __binary_search(self, priority, from_index, to_index):  # find index for priority position
        if from_index > to_index:
            return from_index, True
        else:
            middle_index = (from_index + to_index) // 2
            middle_element = self.__priority_arr[middle_index].priority
            if priority == middle_element:
                return middle_index, False
            elif priority > middle_element:
                return self.__binary_search(priority, middle_index + 1, to_index)
            elif priority < middle_element:
                return self.__binary_search(priority, from_index, middle_index - 1)
