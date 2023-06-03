from src.encrypt import encrypter
from  src.render import *
from src.decrypt import decrypter

print("--------------------------------Begin--------------------------------")

# Make test demo output file

file = encrypter("file.txt")
file_decrypter = decrypter(file)
print(file.read_file())
print(file.return_data_aes())
print(file_decrypter.decrypt())





print("--------------------------------End--------------------------------")

