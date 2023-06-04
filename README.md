# "CryptoGuard"
**"CryptoGuard"** - is a mobile app that allows users to secure their personal information using cryptographic features. The app provides the user with the tools to encrypt and decrypt data, ensuring that important files and messages are protected.

## The main features of the CryptoGuard app are:

1. **File Encryption**: Users will be able to select and protect their sensitive files and documents using various encryption algorithms such as AES (Advanced Encryption Standard). The application allows the creation of encrypted containers in which users can store and manage their files.

2. **Message Encryption**: The application provides a secure messenger that allows users to exchange encrypted messages. When using "CryptoGuard" to send messages, the text will be automatically encrypted on the sender's device and decrypted on the recipient's device. This ensures the confidentiality of correspondence and protects messages from unauthorized access.

3. **Password Generator**: The application also provides a tool for generating strong passwords. Users will be able to create complex and unique passwords for their online accounts, which increases the security and protection against hacking.

4. **Password storage**: CryptoGuard provides a secure password storage feature. Users can store their passwords in an encrypted database that is only accessible after entering the master password or using biometric authentication (e.g. fingerprint scanner or facial recognition).

5. **Data cleansing**: The app also allows users to securely delete sensitive data from the device. Using special cryptographic algorithms, CryptoGuard ensures that deleted files or data cannot be recovered.

6. **Second Authentication Factor**: The application supports the use of a second authentication factor to increase the security of user accounts. It can be linked to the application or use standard methods such as one-time passwords via SMS or TOTP (Time-based One-Time Password) authenticators.

## Installation

Work in progress...

## Usage

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
from src.decrypt import decrypter

file = encrypter("file.txt")
file.encrypt()
file_decrypter = decrypter("file.bin")
print(file_decrypter.decrypt())

```

Output:

```mathematic
hello world
♦♦♦♦
```

## Supported Platforms
- Windows
- Web (coming soon...)

### Author

[Borusov Illia](https://t.me/illiaborusov)

*2023*
