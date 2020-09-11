class RingBuffer:
    def __init__(self, capacity):
       self.capacity = capacity
       self.storage = []
       self.index = 0

    # ---------> append() <----------
        # IF: current length < capacity
            # insert the item at the end of the list
        # ELSE: it is currently at max length
            # replace current index with item
        # IF: we are not at the end --> aka index < (capacity -1)
            # increment index
        # ELSE: we are at end
            # set index back to 0
    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.insert(len(self.storage), item)
        else:
            self.storage[self.index] = item

        if self.index < self.capacity - 1:
            self.index += 1
        else:
            self.index = 0 

    # ---------> get() <----------
    def get(self):
        return self.storage