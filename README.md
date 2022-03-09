# Encryption-and-Decryption-using-Python
I recently learned about cryptography and several encryption and decryption algorithms using Python. Here is the code for the simplest "Encryption Decryption" little project. The main goal of this project is to learn how to implement various algorithms in Python; nevertheless, there are many better and stronger techniques than this code.

## Outline
* [Cryptography](#cryptography)
* [Terminologies in Cryptography](#terminologies-in-cryptography)
  - [Plain Text](#plain-text)
  - [Cipher Text](#cipher-text)
  - [Encryption](#encryption)
     - [Symmetric Encryption](#symmetric-encryption)
     - [Asymmetric Encryption](#asymmetric-encryption)
     - [Hashing](#hashing)
  - [Decryption](#decryption)
* [Installation](#installation)
* [Encryption](#encryption)
  - [Algorithm](#algorithm)
  - [Python code](#python-code)
* [Decryption](#decryption)
  - [Algorithm](#algorithm)
  - [Python code](#python-code)
* [Conclusion](#conclusion)
* [Contribution](#contribution)

## Cryptography

Cryptography is defined as the art and science of concealing the message to introduce privacy and secrecy as recognized in information security.

Cryptography is traditionally used to hide messages from the eyes of certain users. Today, this use has an even greater advantage since communications via the Internet circulate in infrastructures whose reliability and confidentiality cannot be guaranteed. Cryptography is now used not only to protect the confidentiality of data but also to guarantee its integrity and authenticity.

## Terminologies in Cryptography
### Plain Text
The plain text message is the text which is readable and can be understood by all users. The plain text is the message which undergoes cryptography.

### Cipher Text
Cipher text is the message obtained after applying cryptography on plain text.

### Encryption
Encryption is the process of encoding the data. i.e converting plain text into ciphertext. This conversion is done with a key called an encryption key.

There are several data encryption approaches available to choose from. 

#### Symmetric Encryption
Also called private-key cryptography or a secret key algorithm, this method requires the sender and the receiver to have access to the same key. So, the recipient needs to have the key before the message is decrypted. This method works best for closed systems, which have less risk of a third-party intrusion.

#### Asymmetric Encryption
Also called public-key cryptography, this method uses two keys for the encryption process, a public and a private key, which are mathematically linked. The user employs one key for encryption and the other for decryption, though it doesn’t matter which you choose first.

#### Hashing
Hashing generates a unique signature of fixed length for a data set or message. Each specific message has its unique hash, making minor changes to the information easily trackable. Data encrypted with hashing cannot be deciphered or reversed back into its original form. That’s why hashing is used only as a method of verifying data.

### Decryption
Decryption is a process of decoding the encoded data. Converting the ciphertext into plain text. This process requires a key that we used for encryption.

## Installation
You require python IDE on your laptop/PC.

## Encryption
### Algorithm


