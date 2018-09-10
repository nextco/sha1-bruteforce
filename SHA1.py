# Python 2.7 x86
# Simple SHA1 Bruteforce work with dictionary of numbers, the length of the password is known
# by @rextco
from functools import reduce
import hashlib
import itertools
import string       # digits

TARGET_HASH = "8e2b0f24e6f22012b834bde961cc4cc1bb6c6880"                # SHA1 to broke
TARGET_LENGTH = 8                                                       # Password length


def bruteforce():
    seed = string.digits                                              # semilla (numbers)
    # seed = "2013456789"                                                 # if you know the order of bytes just alter it
    seed_bytes = list(map(ord, seed))
    print("seed_bytes = %s" % seed_bytes)

    # Possible are: permutations, combinations or product
    attempts = 0
    for word_bytes in itertools.product(seed_bytes, repeat=TARGET_LENGTH):
        word_string = reduce(lambda x, y: x+y, map(chr, word_bytes))        # word_bytes to string
        hash_ = hashlib.sha1(word_string).hexdigest()                       # SHA1 of word_bytes
        # hash_ = hashlib.sha1(hash_).hexdigest()                           # SHA1 again of prev SHA1

        #  print(word_string, hash_)
        if hash_ == TARGET_HASH:
            print("\n==> Founded: Word = %s | Hash = %s" % (word_string, hash_))
            break

        # Just for debug to check if python is alive xD
        if attempts % (1 << 20) == 0:           # Show print every 1 << 20 attempts
            print("debug!control: Word = %s | Hash = %s | attempts = %d" % (word_string, hash_, attempts))

        attempts += 1


if __name__ == "__main__":
    bruteforce()

