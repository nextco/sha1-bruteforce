# Python 2.7 x86
# Simple MD5 Bruteforce work with dynamic dictionary one memory,
# the length of the password is known
# by @rextco
from functools import reduce
import hashlib
import itertools
import string       # digits

TARGET_HASH = "ac43bb53262e4edd82c0e82a93c84755"                        # MD5 to broke
TARGET_LENGTH = 6                                                       # Password length


def bruteforce():
    seed = string.ascii_lowercase + string.digits                                       # semilla (numbers)
    # seed = "2013456789"                                                # if you know the order of bytes just alter it
    seed_bytes = list(map(ord, seed))
    print("seed_bytes = %s" % seed_bytes)

    # Possible are: permutations, combinations or product
    attempts = 0
    for word_bytes in itertools.product(seed_bytes, repeat=TARGET_LENGTH):
        word_string = reduce(lambda x, y: x+y, map(chr, word_bytes))        # word_bytes to string
        hash_ = hashlib.md5(word_string).hexdigest()                        # MD5 of word_bytes

        if hash_ == TARGET_HASH:
            print("\n==> Founded: word = %s | hash = %s" % (word_string, hash_))
            break

        # Just for debug to check if python is alive xD
        if attempts % (1 << 20) == 0:           # Show print every 1 << 20 attempts
            print("debug!control: word = %s | hash = %s | attempts = %d" % (word_string, hash_, attempts))

        attempts += 1


if __name__ == "__main__":
    bruteforce()

