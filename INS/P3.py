import hashlib
from unittest import result

result1 = hashlib.md5(b"Nero")
print(f"Byte equivalent of hash is: {result1.digest()}")
