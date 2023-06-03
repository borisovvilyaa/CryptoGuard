from src.encrypt import encrypter
from  src.render import *

print("--------------------------------Begin--------------------------------")

# Make test demo output file

file = encrypter("file.txt")

print(file.read_file())

print(file.get_password())

# print(file.return_name())
# print(file.return_src())
# print(file.return_dest())

# file.replace()

# print_directory_files("encrypt")


# file.undo_replace()



print("--------------------------------End--------------------------------")

