# PythonGUIFileEncryptorAndDecryptor


# Requirements:
cryptography package


# To install cryptography package, in cmd, type:
python -m pip install cryptography

# Also before running the program, generate a salt by running the following command in your python shell:
import os

a=os.urandom(16)

print(a)


And copy the returned value and paste it in the program in the line stating: salt=b'salt', replace "b'salt'" with the copied value.
