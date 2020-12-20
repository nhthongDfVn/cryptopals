import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64encode,b64decode
import string
import random

def detect(line):
    k=32
    arr=[line[i:i+k] for i in range(0,len(line),k)]
    myset=set(arr)
    if len(arr)!=len(myset):
        return True
    else:
        return False
def brute(detect):
    global alphatbet
    k=32
    block=3  # set your block want to cmp
    unknown=b''
    privblock=b''
    numlen=detect+1+16*2+15  # set numlen
    while True:
        ok=0
        if numlen==-1:
            block+=1
            numlen=15
            privblock=unknown
            unknown=b''
        cipher=encrypt(b'A'*numlen)
        blocks=[cipher[i:i+k] for i in range(0,len(cipher),k)]
        for char in alphatbet:
            cmp=encrypt(b'A'*numlen+unknown+chr(char).encode())
            blockcmp=[cmp[i:i+k] for i in range(0,len(cmp),k)]
            if blocks[block]==blockcmp[block]:
                unknown+=chr(char).encode()
                print(b"[+] "+unknown)
                numlen-=1
                ok=1
                break
        if ok==0:
            break
def encrypt(message):
    global key,unknownstr,yourstr
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(yourstr+message+unknownstr,16))
    return ct_bytes.hex()
def decrypt(enc):
    global key
    enc = bytes.fromhex(enc)
    cipher = AES.new(self.key, AES.MODE_ECB)
    return unpad(cipher.decrypt(enc)).decode('utf8')

alphatbet=b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=os.urandom(16)
yourstr=b'nht'
#yourstr=b64decode(yourstr)

#create unknow string with unknow length
n=random.randint(8,20)
unknownstr=''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
unknownstr=unknownstr.encode()
print (b"Unknown str:" +unknownstr)


# try to decrypt
for i in range (0,10000):
    tmp=encrypt(b'A'*i)
    if detect(tmp):
        print("Find with length: "+str(i-33))
        brute(i-33)
        break
