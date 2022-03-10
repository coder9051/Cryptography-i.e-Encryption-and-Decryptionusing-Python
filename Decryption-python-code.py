# Create a function for Decryption algorithm
def decrpyt_message(text, key):

    decrypted_msg = "" # initially empty string is created

    for char in text:    

        if char.isupper(): # check character is uppercase
            decrypted_msg += chr((((ord(char) - key) - 65) % 26) + 65)

        elif char.islower(): # checks character is  lowercase
            decrypted_msg += chr((((ord(char) - key) - 97) % 26) + 97)

        else:
            decrypted_msg += char # Number, spaces and special charcters are added as it is.

    return decrypted_msg

text = input("Please Enter your message: ") 
key = int(input("Enter key value: "))

print("Your message: ", text)

decrpyted_message = decrpyt_message(text, key)
print("The Decrypted message is: ", decrpyted_message)
