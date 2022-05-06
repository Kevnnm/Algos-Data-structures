#!/usr/bin/env python3

from primes import erastosthenes_sieve
from word_correction import candidates


# Simple Linked List implementation
class LL:
    def __init__(self, node):
        self.node: Node = node
        self.len = 1


class Node:
    def __init__(self, val: any):
        self.next = None
        self.data = val


class HashTable:
    def __init__(
            self, initial_words: [str],
            collision_resolution_method: str = "linear_probing",
            upper_bound: int = 1000000
    ):
        # Calculate primes beforehand and store it up to dict_limit
        # At a limit of one billion items the number of primes needed is only 22.
        # Note: it was part of the assignment statement to only use primes for HashTable sizes
        self.primes = erastosthenes_sieve(upper_bound)
        self.dict_limit = self.primes[-1]

        # Table features
        self.table_size = self.find_prime(len(initial_words) // 5)
        self.num_keys = 0
        print(f'initial size: {self.table_size}')

        # collision resolution
        if collision_resolution_method == "linear_probing":
            self.dictionary = [None] * self.table_size
            self.collision_resolution = collision_resolution_method
        elif collision_resolution_method == "separate_chaining":
            self.dictionary = []
            for i in range(self.table_size):
                self.dictionary.append(LL(None))
            self.collision_resolution = collision_resolution_method
        else:
            raise ValueError('collision_resolution_method must be "linear_probing" or "separate_chaining"')

        # Statistics
        self.expanded_times = 0
        self.num_collisions = 0
        self.l_collision_chain = 0
        self.current_load_factor = 0

        # initialize
        for word in initial_words:
            self.insert(word)

    def maybe_expand(self):
        # check if expansion is necessary
        self.current_load_factor = self.num_keys / self.table_size
        if self.current_load_factor > 0.5:
            # expand
            expand = getattr(self, self.collision_resolution + "_expand")
            expand()
            self.expanded_times += 1

    def linear_probing_expand(self):
        # expansion for linear probing
        self.l_collision_chain = 0
        self.num_collisions = 0
        self.num_keys = 0

        self.table_size = self.find_prime(self.table_size * 2)
        # self.table_size = self.table_size * 2
        old_array = self.dictionary
        # reset dictionary to twice original size
        self.dictionary = [None] * self.table_size
        for key in old_array:
            if key is None:
                continue
            self.insert(key)

    def separate_chaining_expand(self):
        # expansion for separate chaining
        self.l_collision_chain = 0
        self.num_collisions = 0
        self.num_keys = 0

        self.table_size = self.find_prime(self.table_size * 2)
        # self.table_size = self.table_size * 2
        old_array = self.dictionary
        # reset dictionary to twice original size
        self.dictionary = []
        for i in range(self.table_size):
            self.dictionary.append(LL(None))

        for key in old_array:
            n = key.node
            if n is None:
                continue
            else:
                # reinsert all keys in bucket
                while n is not None:
                    self.insert(n.data)
                    n = n.next

    def insert(self, word: str):
        hash_value = self.hash(word)
        # collision resolution specific insert
        ins = getattr(self, self.collision_resolution + "_set")
        ins(word, hash_value)

        # check to expand
        self.maybe_expand()

    def linear_probing_set(self, word: str, hash_value):
        # set value for linear probe
        if self.dictionary[hash_value] is None:
            self.num_keys += 1
            self.dictionary[hash_value] = word
        else:
            # linear probe resolving
            resolution = getattr(self, self.collision_resolution + "_resolution")
            resolution(word, hash_value)

    def linear_probing_resolution(self, word, hash_value):
        # linear probing
        collision_chain = 0

        # increment hash_value until dictionary[hash_value] is none
        while self.dictionary[hash_value]:
            # repeat key checking
            if self.dictionary[hash_value] == word:
                return

            collision_chain += 1
            hash_value += 1
            # bounds checking
            if hash_value >= self.table_size:
                hash_value = 0

        # stats
        if collision_chain > self.l_collision_chain:
            self.l_collision_chain = collision_chain
        self.num_collisions += collision_chain

        # assignment
        self.num_keys += 1
        self.dictionary[hash_value] = word

    def separate_chaining_set(self, word: str, hash_value: int):
        # set value for separate chaining collision resolution
        if self.dictionary[hash_value].node is None:
            self.num_keys += 1
            self.dictionary[hash_value].node = Node(word)
        else:
            # separate chaining via linked lists
            resolution = getattr(self, self.collision_resolution + "_resolution")
            resolution(word, hash_value)
            # we know a collision has occurred
            self.num_collisions += 1

    def separate_chaining_resolution(self, word: str, hash_value: int):
        # head node
        n = self.dictionary[hash_value].node
        # repeat key checking
        if n.data == word:
            return
        # advance node until last node
        while n.next is not None:
            n = n.next
            # repeat key checking
            if n.data == word:
                return

        # append node
        self.num_keys += 1
        n.next = Node(word)

        # stats
        self.dictionary[hash_value].len += 1
        if self.dictionary[hash_value].len > self.l_collision_chain:
            self.l_collision_chain = self.dictionary[hash_value].len

    def in_dict(self, word):
        # use collision resolutions specific get
        hash_value = self.hash(word)
        get = getattr(self, self.collision_resolution + "_get")
        return get(word, hash_value)

    def linear_probing_get(self, word: str, hash_value):
        # advance until no value
        while self.dictionary[hash_value] is not None:
            # bounds checking
            if hash_value >= self.table_size - 1:
                hash_value = 0

            # compare
            if self.dictionary[hash_value] == word:
                return True

            hash_value += 1

        return False

    def separate_chaining_get(self, word: str, hash_value: int):
        # head node
        n = self.dictionary[hash_value].node

        # advance until no node
        while n is not None:
            # compare
            if n.data == word:
                return True

            n = n.next

        return False

    # search primes array for primes larger than 'larger_than'
    def find_prime(self, larger_than: int):
        for p in self.primes:
            if p > larger_than:
                return p

        return -1

    # hashing function
    def hash(self, s: str):
        """Hashing function to be used"""
        h = 0
        for ch in s:
            h *= 37
            h += ord(ch)
        return h % self.table_size

    def candidates(self, word):
        """Specifically for the dictionary assignment."""
        c = candidates(word, self.known)
        # return all correction candidates for given word
        return c

    # takes a list of words and returns words in dictionary
    def known(self, words: [str]):
        known_words = []
        for word in words:
            hash_value = self.hash(word)

            get = getattr(self, self.collision_resolution + "_get")
            is_word = get(word, hash_value)
            if is_word:
                known_words.append(word)

        return known_words


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
