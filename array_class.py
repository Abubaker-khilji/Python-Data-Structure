class array_class:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            print("Index out of bounds")

    def display(self):
        print(self.array)

# Example Usage
if __name__ == "__main__":
    arr = array_class(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    arr.display()
