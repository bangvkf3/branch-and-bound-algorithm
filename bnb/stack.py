class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise PopEmptyStackError()
        return self.items.pop()


class PopEmptyStackError(Exception):
    def __str__(self):
        return "비어있는 스택에서 pop 연산"
