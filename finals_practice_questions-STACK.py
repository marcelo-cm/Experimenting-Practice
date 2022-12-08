class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1] #get the last element
    def __str__(self):
        return str(self.items)
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
             source1 - an array-based stack (Stack)
             source2 - an array-based stack (Stack)
        Returns:
             None
        -------------------------------------------------------
        """
        while len(source1) > 0 and len(source2) > 0:
            self.push(source1.pop())
            self.push(source2.pop())
        if len(source1) > 0:
            for i in source1:
                self.push(i)
        if len(source2) > 0:
            for i in source2:
                self.push(i)

def split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks with values
    alternating into the targets. At finish, the source stack is empty.
    Use: target1, target2 = split_alt(source)
    -------------------------------------------------------
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 =  []
    target2 = []
    for i in range(len(source.items)):
        if i % 2 == 0:
            target1.append(source.pop())
        else:
            target2.append(source.pop())
    return (target1, target2)

print("Stack example:")
s = Stack()
s.push(1)
s.push(3)
s.push(5)
s.push(7)
print(s, "\n")

target1, target2 = split_alt(s)
print(target1, target2)
print(s, "\n")

s.combine(target1, target2)
print(s)