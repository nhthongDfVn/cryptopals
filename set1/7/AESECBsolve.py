from Crypto.Cipher import AES
from base64 import b64decode
f= open("7.txt","r")
encrypt=''
key=b'YELLOW SUBMARINE'
for line in f:
    encrypt+=line.strip('\n')
#print (encrypt)
encrypt=b64decode(encrypt)
plaintext=AES.new(key, AES.MODE_ECB)
print(plaintext.decrypt(encrypt))
