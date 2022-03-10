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
* [Encryption Python Code](#encryption-python-code)
* [Decryption Python Code](#decryption-python-code)
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

## Encryption Python Code
The plain text character is traversed one at a time. Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet. After the steps is followed, a new string is generated which is referred as cipher text. This algorithm is known as "Caeser Cipher".
```python
# Create a function for Encryption algorithm
def encrpyt_message(text, key):
    encrypted_msg = "" # initially empty string is created
    for char in text:
    
        if char.isupper(): # check character is uppercase
            encrypted_msg += chr((((ord(char) + key) -65) % 26) + 65)

        elif char.islower(): # checks character is  lowercase
            encrypted_msg += chr((((ord(char) + key) -97) % 26) + 97)
            
        else:
            encrypted_msg += char # Number, spaces and special charcters are added as it is.

    return encrypted_msg
    
text = input("Please Enter your message: ") 
key = int(input("Enter key value: "))

print("Your message: ", text)

encrpyted_message = encrpyt message(text, key)

print("The Encrypted message is: ", encrpyted_message)
```

## Decryption Python Code
This code can only be used when we know key else we have try brute force method by trying for every key value. In this method we undo the previous code to get original message.

```python
#Create a function for Decryption algorithm
def decrpyt_message(text, key):

    decrypted_msg = "" # initially empty string is created

    for char in text:    

        if char.isupper(): # check character is uppercase
            decrypted_msg += chr((((ord(char) - key) - 65) % 26) + 65)

        elif char.islower(): # checks character is  lowercase
            decrypted_msg += chr((((ord(char) -key) - 97) % 26) + 97)

        else:
            decrypted_msg += char # Number, spaces and special charcters are added as it is.

    return decrypted_msg

text = input("Please Enter your message: ") 
key = int(input("Enter key value: "))

print("Your message: ", text)

decrpyted_message = decrpyt_message(text, key)
print("The Decrypted message is: ", decrpyted_message)
```

## Conclusion
