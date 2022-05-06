#!/usr/bin/env python3

from bst import Node, BST

with open("users7.txt") as f:
    content = f.readlines()

bst = BST()
for s in content:
    s = s.strip("\n")
    user_split = s.split(" ")
    if len(user_split) != 2:
        continue
    else:
        bst.insert(Node(user_split[0], user_split[1]))

while True:
    username = input("Please enter your username: ")
    node = bst.find(username)
    if node is not None:
        tries = 0
        failed = True
        while tries < 3:
            password = input("Please enter you password: ")
            if node.password == password:
                print("Congrats you are authenticated")
                failed = False
                break
            else:
                print("Bad login")
                tries += 1
        if failed:
            print("login failed: removing user")
            bst.remove(username)
    else:
        print("Bad login")
