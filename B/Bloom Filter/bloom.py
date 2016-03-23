"""This module implements a bloom filter probabilistic data structure"""

#from __future__ import absolute_import
import math
import hashlib
from struct import unpack, pack, calcsize
