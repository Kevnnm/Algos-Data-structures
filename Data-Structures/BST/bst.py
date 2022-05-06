#!/usr/bin/env python3

class Node:
    def __init__(self, username_in, password_in):
        self.left = None
        self.right = None
        self.username = username_in
        self.password = password_in


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        if new_node.username <= current_node.username:
            if current_node.left is not None:
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.username > current_node.username:
            if current_node.right is not None:
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def find(self, username):
        return self.__find_node(self.root, username)

    def __find_node(self, current_node, username):
        if current_node.username == username:
            return current_node
        elif username < current_node.username and current_node.left is not None:
            return self.__find_node(current_node.left, username)
        elif username > current_node.username and current_node.right is not None:
            return self.__find_node(current_node.right, username)

        return None

    def parent(self, username):
        return self.__parent(self.root, None, username)

    def __parent(self, current_node, current_parent, username):
        if current_node.username == username:
            return current_parent
        elif username < current_node.username and current_node.left is not None:
            p = self.__parent(current_node.left, current_node, username)
        elif username > current_node.username and current_node.right is not None:
            p = self.__parent(current_node.right, current_node, username)

        return p

    def remove(self, username):
        self.__remove(self.root, username)

    def __remove(self, current_node, username):
        if not current_node:
            return current_node

        if current_node.username > username:
            current_node.left = self.__remove(current_node.left, username)
        elif current_node.username < username:
            current_node.right = self.__remove(current_node.right, username)
        else:
            if not current_node.right:
                return current_node.left
            if not current_node.left:
                return current_node.right

            temp_val = current_node.right
            while temp_val.left:
                temp_val = temp_val.left
            if temp_val:
                current_node.username = temp_val.username
                current_node.password = temp_val.password
            else:
                current_node = None

            current_node.right = self.__remove(current_node.right, temp_val.username)

        return current_node

    def is_empty(self):
        if self.root is None:
            return True

        return False

    def preorder(self):
        return self.__preorder(self.root, [])

    def __preorder(self, current_node, out_list):
        out_list.append(current_node)
        if current_node.left is not None:
            self.__preorder(current_node.left, out_list)
        if current_node.right is not None:
            self.__preorder(current_node.right, out_list)

        return out_list

    def inorder(self):
        return self.__inorder(self.root, [])

    def inorder_internal(self, node):
        if node is None:
            return None
        return self.__inorder(node, [])

    def __inorder(self, current_node, out_list):
        if current_node.left is not None:
            self.__inorder(current_node.left, out_list)
        out_list.append(current_node)
        if current_node.right is not None:
            self.__inorder(current_node.right, out_list)

        return out_list

    def postorder(self):
        return self.__postorder(self.root, [])

    def __postorder(self, current_node, out_list):
        if current_node.left is not None:
            self.__postorder(current_node.left, out_list)
        if current_node.right is not None:
            self.__postorder(current_node.right, out_list)

        out_list.append(current_node)
        return out_list

    def print(self):
        self.__print_subtree(self.root, 0)

    def __print_subtree(self, current_node, level):
        if current_node is not None:
            self.__print_subtree(current_node.right, level + 1)
            for i in range(3 * level):
                print(" ", end="")
            print(current_node.username)
            self.__print_subtree(current_node.left, level + 1)

    def count(self):
        return self.__count(self.root, 0)

    def __count(self, current_node, count):
        left_count = 0
        right_count = 0
        if current_node.left:
            left_count = self.__count(current_node.left, count)
        if current_node.right:
            right_count = self.__count(current_node.right, count)

        return left_count + right_count + 1

    def trim(self, mini, maximum):
        traversal = self.inorder()
        for node in traversal:
            if node.username and not mini <= node.username <= maximum:
                self.remove(node.username)


def main():
    usernames = ["i", "love", "you", "pca", "is", "easy", "happy", "day", "kmitl"]

    bst = BST()
    for names in usernames:
        bst.insert(Node(names, ""))

    bst.remove("pca")
    bst.trim("eee", "love")

    bst.print()
    print(bst.count())
    print([i.username for i in bst.inorder()])
    print([i.username for i in bst.preorder()])
    print([i.username for i in bst.postorder()])


if __name__ == '__main__':
    main()
