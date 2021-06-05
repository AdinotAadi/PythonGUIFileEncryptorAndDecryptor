#Python GUI Based FIle Encryptor and Decryptor


# Importing Modules
from tkinter import *
from tkinter import messagebox
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Defining Window
root = Tk()
root.title("File Encryptor And Decryptor")
root.geometry("640x360+600+300")


# Generate Using A Key From 'os.urandom(16)', Must Be Of 'byte' Data Type
salt = b'salt'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)


# Defining Functions
def decrypt():
    global key, message
    # Decrypting Message
    encoded = message.encode()
    f2 = Fernet(key)
    encrypted = f2.encrypt(encoded)
    f4 = Fernet(key)
    dercypted = f4.decrypt(encrypted)
    # Decode Message
    original_message = dercypted.decode()
    f5 = open("DecryptedData.txt", 'w')
    f5.write(original_message)
    f5.close()
    # Decrypting Complete File
    f8 = open("test.ncryptd", 'rb')
    data2 = f8.read()
    fernet = Fernet(key)
    decrypted1 = fernet.decrypt(data2)
    f8.close()
    # Writing To A Decrypted File
    f9 = open("test.dcryptd", 'wb')
    f9.write(decrypted1)
    messagebox.showinfo("Alert!", "File Decrypted. \nMessage in bytes is:\n\n"+str(decrypted1)[2:-1])
    f9.close()


def encrypt():
    global key, message
    # Encode Message
    message = Msg.get()
    print(message)
    msg = str.encode(message)
    test = open("test.txt", 'wb')
    test.write(msg)
    test.close()
    encoded = message.encode()
    # Encrypting Message
    f2 = Fernet(key)
    encrypted = f2.encrypt(encoded)
    f3 = open("EncryptedData.txt", 'wb')
    f3.write(encrypted)
    f3.close()
    messagebox.showinfo("Alert!", '''Message Encrypted! \nDelete Original File If Necessary.''')
    # Encrypting Complete File
    f6 = open("test.txt", 'rb')
    data1 = f6.read()
    fernet = Fernet(key)
    encrypted1 = fernet.encrypt(data1)
    f6.close()
    # Writing To An Encrypted File
    f7 = open("test.ncryptd", 'wb')
    f7.write(encrypted1)
    f7.close()


# Defining Variables
MasterPass = Label(root, text="Enter Master Password")
MasterPass.grid(row=0, column=0, sticky=N+S+W+E)
MPass = StringVar()
MPassEntry = Entry(root, textvariable=MPass)
MPassEntry.grid(row=0, column=1, sticky=N+S+W+E)
global Pass
Pass = MPass.get()
global password
password = Pass.encode()
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can Use kdf Only Once
print(key)

Message = Label(root, text="Enter Message:")
Message.grid(row=2, column=0, sticky=N+S+W+E)
Msg = StringVar()
MsgEntry = Entry(root, textvariable=Msg)
MsgEntry.grid(row=2, column=1, sticky=N+S+W+E)
print(Msg.get())


# Storing The Key To A File
f1 = open("key.key", 'wb')
f1.write(key)
f1.close()

EncrButton = Button(root, text="Encrypt", width=14, command=encrypt)
EncrButton.grid(row=0, column=3, sticky=N+S+W+E)

DecrButton = Button(root, text="Decrypt", width=14, command=decrypt)
DecrButton.grid(row=2, column=3, sticky=N+S+W+E)

# Making The UI Responsive
TotRows = 3
TotColumns = 3

for i in range(TotRows+1):
    root.grid_rowconfigure(i, weight=1)

for j in range(TotColumns+1):
    root.grid_columnconfigure(j, weight=1)


root.mainloop()
