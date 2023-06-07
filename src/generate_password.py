import hashlib
from random import randint
def generate_password() -> str:
    s = str(randint(10000, 100000))
    h = hashlib.new("ripemd160")
    h.update(s.encode("utf-8"))
    return h.hexdigest()
