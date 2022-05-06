class Stack:
    def __init__(self):
        # Init empty stack
        self.stack = []

    def is_empty(self):
        # If array is empty return True
        if len(self.stack) == 0:
            return True

        return False

    def size(self):
        return len(self.stack)

    def push(self, element):
        # Append
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        # Save last element
        last_elem = self.stack[-1]
        # Remove last element
        self.stack = self.stack[:-1]
        # Return last element
        return last_elem

    def peek(self):
        if self.is_empty():
            return None
        # Return last element but don't remove
        return self.stack[-1]

    def contain(self, element):
        # If element is in the list return True
        if element in self.stack:
            return True

        return False


class ValetPark:
    def __init__(self, cars: Stack):
        self.cars = cars

    def remove_car(self, value):
        """Removes the the element with value"""
        temp = Stack()
        while self.cars.peek() != value:
            if self.cars.is_empty():
                break
            temp.push(self.cars.pop())

        rm = self.cars.pop()

        for i in temp.stack:
            self.cars.push(temp.pop())

        return rm


def main():
    # Initializing Stack instance
    st1 = Stack()

    # Push elements into stack
    st1.push("car1")
    st1.push("car2")
    st1.push("car3")
    st1.push("car4")

    vp = ValetPark(st1)
    vp.remove_car("car3")
    print(vp.cars.stack)


if __name__ == '__main__':
    main()
