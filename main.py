from src.encrypt import encrypter
from  src.render import *
from src.decrypt import decrypter

print("--------------------------------Begin--------------------------------")

# Make test demo output file

file = encrypter("file.txt")
file.encrypt()
file_decrypter = decrypter("file.bin")
print(file_decrypter.decrypt())

print("--------------------------------End--------------------------------")

