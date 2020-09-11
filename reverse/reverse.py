class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    # --------> reverse_list() <---------
        # IF: list is empty
            # return None
        # IF: length is 1
            # return 
        # ELSE: ... list length > 1 & items need to be reversed
            # capture necessary variables
                # current_node
                # previous_node
                # next_node
            # WHILE: not the last or 2nd-to-last value
                # current_node's next (set_next()) should be the previous_node
                # previous_node should become current_node
                # current_node becomes item that was after it (next_node)
                # next_node becomes the previous next value (current_node.get_next())
            # once at the second to last node...
                # current_node next should be the previous_node
                # head should become 'next_node" (last value in list)
                # new head needs to be connected to current_node -- (set_next)

    def reverse_list(self, node, prev):
        if self.head is None:   # list is empty
            return None
        if self.head.get_next() is None:    # list length is 1
            return
        else:
            current_node = node
            previous_node = prev
            next_node = node.get_next()

            while next_node.get_next() is not None:
                current_node.set_next(previous_node)
                previous_node = current_node
                current_node = next_node
                next_node = current_node.get_next()

            # we are at 2nd-to-last node once we get here
            current_node.set_next(previous_node)
            self.head = next_node
            self.head.set_next(current_node)
