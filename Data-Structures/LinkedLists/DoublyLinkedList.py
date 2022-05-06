class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, name, score):
        new_node = TwoWayNode(GolferScore(name, score))
        if self.head is not None and self.head.data.score > score:
            self.head.set_previous(new_node)
            new_node.set_next(self.head)
            self.head = new_node
            return new_node
        elif self.last is not None and self.last.data.score < score:
            self.last.set_next(new_node)
            new_node.set_previous(self.last)
            self.last = new_node
            return new_node
        elif self.last is None and self.head is None:
            self.last = new_node
            self.head = new_node
            return new_node

        current = self.head.get_next()
        prev = self.head
        while current is not None:
            if current.data.score > score:
                break
            prev = current
            current = current.get_next()

        if current is not None:
            new_node.set_next(current)
            current.set_previous(new_node)

            new_node.set_previous(prev)
            prev.set_next(new_node)

        return new_node

    def remove(self, name):
        if self.head is None and self.last is None:
            return

        if self.head is not None and self.head.data.name == name:
            self.head = self.head.get_next()
            return
        elif self.last is not None and self.last.data.name == name:
            self.last = self.last.get_previous()
            return

        current = self.head.get_next()
        prev = self.head
        while current is not None:
            if current.data.name == name:
                break
            prev = current
            current = current.get_next()

        if current is not None:
            prev.set_next(current.get_next())
            current.get_next().set_previous(prev)

    def update(self, name, score):
        current = self.head
        while current is not None:
            if current.data.name == name:
                break
            current = current.get_next()

        if current:
            current.data.score = score

    def print_ascending(self):
        current = self.head
        while current is not None:
            print(f'{current.data.name}: {current.data.score}')
            current = current.get_next()

    def print_descending(self):
        current = self.last
        while current is not None:
            print(f'{current.data.name}: {current.data.score}')
            current = current.get_previous()

    def print_same_scores(self, name):
        current = self.head
        while current is not None:
            if current.data.name == name:
                break
            current = current.get_next()

        print(f'All players with score of {current.data.score}:')
        if current is not None:
            center = current
            while current is not None and current.data.score == center.data.score:
                print(current.data.name)
                current = current.get_previous()

            current = center.get_next()
            while current is not None and current.data.score == center.data.score:
                print(current.data.name)
                current = current.get_next()


class TwoWayNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, next_node):
        self.next = next_node

    def set_previous(self, previous_node):
        self.previous = previous_node


class GolferScore:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def main():
    dbl = DoublyLinkedList()
    dbl.insert("Pease", 74)
    dbl.insert("Walker", 76)
    dbl.insert("MacKay", 77)
    dbl.insert("Klomps", 76)

    dbl.print_ascending()
    # dbl.print_descending()

    dbl.print_same_scores("Walker")


if __name__ == '__main__':
    main()
