#!/usr/bin/env python3

def erastosthenes_sieve(n: int) -> [int]:
    """
    Special implementation of the Sieve of Eratosthenes where only the primes that are twice as large as the previous prime is returned.

    :arg n: upper limit
    """
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    ret = []
    p = 2
    while p << 1 <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p << 1, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    # Only grab primes that are at least 2 as large as the previous prime
    previous_prime = 0
    for p in range(n + 1):
        if prime[p] and previous_prime << 1 < p:
            previous_prime = p
            ret.append(p)

    return ret


if __name__ == '__main__':
    n = 1000000
    print("Following are the prime numbers smaller")
    print("than or equal to ", n)
    primes = erastosthenes_sieve(n)
    print(len(primes))
    for p in primes:
        print(p)
