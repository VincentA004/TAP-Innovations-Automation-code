from cryptography.fernet import Fernet
import os


with open('Cals_pwds.txt') as f:
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
if os.path.exists("Cals_pwds.txt"):
  os.remove("Cals_pwds.txt")
else:
  print("File is not available")