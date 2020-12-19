#sử dụng XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX lớn hơn 32
#để kiểm tra
from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
import random

def ECBencrypt(message):
    global key
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(message,16))
    return ct_bytes.hex()
def CBCencrypt(message):
    global key
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message, 16))
    return ct_bytes.hex()
def detect(line):
    n=32
    arr=[line[i:i+n] for i in range(0,len(line),n)]
    myset=set(arr)
    if len(arr)!=len(myset):
        print ("Using ECB to encrypt")
    else:
        print ("Using CBC to encrypt")
key=os.urandom(16)
message=input("Your message: ")
message=message.encode()
message=os.urandom(9)+message+os.urandom(8)
res=b''
if random.randint(1,2)==1:
    res=ECBencrypt(message)
else:
    res=CBCencrypt(message)
print (res)
detect(res)
