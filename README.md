![IMG5](https://user-images.githubusercontent.com/84984325/125477542-ed2a00de-2a5d-4337-9cfa-0916851a01ff.png)
# PythonGUIFileEncryptorAndDecryptor


# Requirements:
cryptography package


# To install cryptography package, in cmd, type:
python -m pip install cryptography

# Also before running the program, generate a salt by running the following command in your python shell:
import os

a=os.urandom(16)

print(a)


# Copy the returned value and paste it in the program in the line stating: salt=b'salt', replace "b'salt'" with the copied value.
