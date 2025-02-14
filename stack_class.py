class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

# Example Usage
if __name__ == "__main__":
    st = Stack()
    st.push(5)
    st.push(10)
    st.push(15)
    st.display()
    print("Popped:", st.pop())
    st.display()
