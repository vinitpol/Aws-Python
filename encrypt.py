    
from cipherkey import getcipherkey
from message import getmessage

def encryptmessage(message, cipherkey, alphabet):
    encryptedmessage = ""
    uppermessage = message.upper()
    for char in uppermessage:
        if char in alphabet:
            position = alphabet.find(char)
            newpost = position + int(cipherkey) 
            encryptedmessage += alphabet[newpost]
        else:
            encryptedmessage += char
    return encryptedmessage

def decrypmessage(encryptedmessage, cipherkey, alphabet):
    decryptedmessage = ""
    uppermessage = encryptedmessage.upper()
    for char in uppermessage:
        if char in alphabet:
            position = alphabet.find(char)
            newpost = position - int(cipherkey)
            decryptedmessage += alphabet[newpost]
        else:
            decryptedmessage += char
    return decryptedmessage

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = getcipherkey()
m = getmessage()

print("To Encrypt the Message")
print(encryptmessage(m, c, a))

print("To Decrypt the Message")
print(decrypmessage(encryptmessage(m, c, a), c, a))
