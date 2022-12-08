class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def __str__(self):
        return str(self.items)

    def  is_identical(self, target):
        """
        ----------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: identical = source.is_identical(target)
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False otherwise.
                source and target are unchanged. (boolean)
        ---------------
        """
        identical = True
        if len(self.items) != len(target):
            identical = False
            return identical
        for i in range(len(target)):
            if self.items[i] != target[i]:
                identical = False
                return identical
        return identical


print("Queue example:")
q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q, "\n")

identical = q.is_identical([4,5,6,7])
print(identical, "\n")
