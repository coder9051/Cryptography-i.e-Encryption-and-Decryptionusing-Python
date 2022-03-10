# Create a function for Encryption algorithm
def encrpyt_message(text, key):
    encrypted_msg = "" # initially empty string is created
    for char in text:
    
        if char.isupper(): # check character is uppercase
            encrypted_msg += chr((((ord(char) + key) -65) % 26) + 65)

        elif char.islower(): # checks character is  lowercase
            encrypted_msg += chr((((ord(char) + key) -97) % 26) + 97)
            
        else:
            encrypted_msg += char # Numbers, spaces and characters are added as it is.

    return encrypted_msg
