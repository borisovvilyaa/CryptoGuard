from src.encrypt import encrypter
# from src.render import *
from src.decrypt import decrypter

print("--------------------------------Begin--------------------------------")

# Make test demo output file

file = encrypter("file.txt")
print("Password for this file is", file.get_password())
file.encrypt()

# print(file.read_file_utf8())

file_decrypter = decrypter("file.gf", "38e8606c44c0cc3c06cf790f7892c12136912258")
print(file_decrypter.decrypt())

print("--------------------------------End--------------------------------")

