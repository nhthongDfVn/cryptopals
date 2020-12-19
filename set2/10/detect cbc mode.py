from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

iv=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
key=b'YELLOW SUBMARINE'

def decrypt(message):
    try:
        global iv
        raw = b64decode(message)
        print (raw)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(raw), 16)
        print (pt)
    except ValueError:
        print("Incorrect decryption")
def encrypt(message):
    global iv
    cipher = AES.new(key, AES.MODE_CBC,iv)
    ct_bytes = cipher.encrypt(pad(message, 16))
    ct = b64encode(ct_bytes).decode('utf-8')
    return ct

#c=encrypt(b'secrect')
#decrypt(c)
f=open("10.txt","r")
for line in f:
    line=line.strip('\n')
    decrypt(line)
print ("Fi")
