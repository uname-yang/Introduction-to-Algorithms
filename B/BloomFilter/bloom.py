#bloom filter probabilistic data structure
#Yang.Yu
#

import sys
sys.path.append('../..')
import math
import hashlib

from B.BitArray import bitarray

class bloomfilter(object):
    def __init__(self, capacity, error_rate=0.001):
        if not (0 < error_rate < 1):
            raise ValueError("Error_Rate must be between 0 and 1.")
        if not capacity > 0:
            raise ValueError("Capacity must be > 0")
        # given M = num_bits, k = num_of_hashes, P = error_rate, n = capacity
        #       k = log2(1/P)
        # solving for m = bits_per_slice
        # n ~= M * ((ln(2) ** 2) / abs(ln(P)))
        # n ~= (k * m) * ((ln(2) ** 2) / abs(ln(P)))
        # m ~= n * abs(ln(P)) / (k * (ln(2) ** 2))
        num_of_hashes = int(math.ceil(math.log(1.0 / error_rate, 2)))
        bits_per_hash = int(math.ceil((capacity * abs(math.log(error_rate))) /(num_of_hashes * (math.log(2) ** 2))))
        self._setup(error_rate, num_of_hashes, bits_per_hash,capacity, 0)
        self.bitarray = bitarray(self.num_bits)
        self.bitarray.SetAll(False)

    def _setup(self, error_rate, num_of_hashes,bits_per_hash, capacity, count):
        self.error_rate = error_rate
        self.num_of_hashes = num_of_hashes
        self.num_bits=num_of_hashes*bits_per_hash
        self.capacity = capacity
        self.count = count
        self.make_hashes = make_hashfuncs(self.num_of_hashes)
