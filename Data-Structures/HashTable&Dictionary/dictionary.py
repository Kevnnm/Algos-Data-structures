#!/usr/bin/env python3

from hash_table import HashTable


def main():
    file = open("./full.txt")
    s = file.read()
    words = s.split(' ')
    print(f'number of words: {len(words)}')
    table = HashTable(words, "separate_chaining")

    print(f'current load factor: {table.current_load_factor}')
    print(f'number of collisions: {table.num_collisions}')
    print(f'longest collision/largest bucket chain: {table.l_collision_chain}')
    print(f'number of times expanded: {table.expanded_times}')

    print("Dictionary")
    while True:
        word = input("Please enter word to be checked: ")

        is_word = table.in_dict(word)

        if not is_word:
            print(f"{word} is not in the dictionary")
            c = table.candidates(word)
            if len(c) == 0:
                print("No corrections available")
            else:
                print(f"Possible corrections are {c}")
        else:
            print(f"{word} is in the dictionary")


if __name__ == '__main__':
    main()
