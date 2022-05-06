class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def squish(self):
        prev = self.head
        current = self.head.get_next()

        while current is not None:
            if current.get_data() == prev.get_data():
                prev.set_next(current.get_next())
                current = current.get_next()
            else:
                prev = current
                current = current.get_next()

    def double(self):
        current = self.head

        while current is not None:
            temp = current.get_next()
            current.set_next(Node(current.get_data()))
            current.get_next().set_next(temp)
            current = temp

    def __str__(self):
        ret = []
        current = self.head
        while current is not None:
            ret.append(current.get_data())
            current = current.get_next()

        return str(ret)


def main():
    my_list = LinkedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.add(54)
    my_list.add(54)

    print(my_list.search(31))

    my_list.remove(31)
    print(my_list.search(31))
    print(f'size: {my_list.size()}')

    print(f'before squish: {my_list}')
    my_list.squish()
    print(f'after squish: {my_list}')

    print(f'before double: {my_list}')
    my_list.double()
    print(f'after double: {my_list}')


if __name__ == '__main__':
    main()
