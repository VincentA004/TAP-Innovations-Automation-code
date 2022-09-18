from cryptography.fernet import Fernet
import os


with open('MGA_pwds.txt') as f:
    mypwd = ''.join(f.readlines())


key = Fernet.generate_key()
f = open("refKey.txt", "wb")
f.write(key)
f.close()


refKey = Fernet(key)
mypwdbyt = bytes(mypwd, 'utf-8') 
encryptedPWD = refKey.encrypt(mypwdbyt)
f = open("encryptedPWD.txt", "wb")
f.write(encryptedPWD)
f.close()
### 4. delete the password file
if os.path.exists("MGA_pwds.txt"):
  os.remove("MGA_pwds.txt")
else:
  print("File is not available")