# "CryptoGuard"
**"CryptoGuard"** - is a mobile app that allows users to secure their personal information using cryptographic features. The app provides the user with the tools to encrypt and decrypt data, ensuring that important files and messages are protected.

## The main features of the CryptoGuard app are:

1. **File Encryption**: Users will be able to select and protect their sensitive files and documents using various encryption algorithms such as AES (Advanced Encryption Standard). The application allows the creation of encrypted containers in which users can store and manage their files.

2. **Password Generator**: The application also provides a tool for generating strong passwords. Users will be able to create complex and unique passwords for their online accounts, which increases the security and protection against hacking.

3. **Password storage**: CryptoGuard provides a secure password storage feature. Users can store their passwords in an encrypted database that is only accessible after entering the master password or using biometric authentication (e.g. fingerprint scanner or facial recognition).


## Installation

1. Install python
2. Install packages from requirements.txt `pip install -r requirements.txt`
3. Open CMD or Terminal and write commant `python main.py` (Windows) or `python3 main.py` (MacOS, Linux)

## Usage
#### On code
1. Make password for file 

How it works? Class encrypter create hash for password from text file 

```python
from src.encrypt import encrypter

file = encrypter("file.txt")

print(file.read_file())

print(file.get_password())

```

Output:

```mathematic
Hello world!

It's first encrypt

771cbac3c2df85a04de8dba6f104a1177c192dfc
```

2. Make encrypted and decrypted file

```python

from src.encrypt import encrypter
# from src.render import *
from src.decrypt import decrypter

file = encrypter("file.txt")
print("Password for this file is", file.get_password())
file.encrypt()


file_decrypter = decrypter("file.bin", b"38e8606c44c0cc3c06cf790f7892c12136912258")
print(file_decrypter.decrypt())
```

Output:

```mathematic
Password for this file is 38e8606c44c0cc3c06cf790f7892c12136912258
Hello, my name is Illia
```
#### On winwods
1. Encrypt file
1.1 Open program and push _Encrypt_  
![image](https://github.com/borisovvilyaa/CryptoGuard/assets/113841816/93a00062-b20f-46de-b3fb-8092fdfe3ec9)  
1.2 Change another file and open him  
![image](https://github.com/borisovvilyaa/CryptoGuard/assets/113841816/b073e282-792c-4aee-a5db-ebd6bc1d0a5c)  
1.3 In this window can edit text and save him or if push on button `Encrypt end save`, file moved in folder `encrypt` 
1.4 In the end window, we can see password and window about _success_ moving file  
![image](https://github.com/borisovvilyaa/CryptoGuard/assets/113841816/12f5478b-c1fe-4f2e-9c41-08c6aed76507)  
2. Decrypt file  
2.1 When push the button `decrypt`, opening file in format _.gf_  
2.3 Write password for this file, which have on point 1.4  
![image](https://github.com/borisovvilyaa/CryptoGuard/assets/113841816/3cc84c21-9fad-4373-9b21-da7a4df8971a)  
2.4 See encrypt file  
![image](https://github.com/borisovvilyaa/CryptoGuard/assets/113841816/c4261419-d92d-49be-8c74-71a01acddbb1)  

## Supported Platforms
- Windows
- Web (coming soon...)

### Author

[Borusov Illia](https://t.me/illiaborusov)

*2023*
