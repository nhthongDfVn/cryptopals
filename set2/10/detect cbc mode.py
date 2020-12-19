from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import math

iv=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
key=b'YELLOW SUBMARINE'
def _pad(text, block_size):
    no_of_blocks = math.ceil(len(text)/float(block_size))
    pad_value = int(no_of_blocks * block_size - len(text))
    re=b''
    if pad_value == 0:
        re=chr(block_size) * block_size
    else:
        re=chr(pad_value) * pad_value
    return text+re.encode()
def _unpad(ct):
    return ct[:-ord(ct[-1])]
def xor(first,second):
    re=b''
    for i in range(0,len(fi)):
        re+=chr(first[i])^chr(second[i])
    return re
def encryptCBCbyblock(line):
    global iv,key
    ciphertext=b''
    n=16 # size of 1 block
    blocks=[line[i:i+n] for i in range(0,len(line),n)]
    #encrypt
    priv=iv
    for block in blocks:
        if len(block)!=16:
            block=_pad(block,16)
        cipher = AES.new(key, AES.MODE_CBC,priv)
        ct_bytes = cipher.encrypt(block)
        priv=ct_bytes
        ciphertext+=ct_bytes
    print(b64encode(ciphertext).decode('utf-8'))
def decryptCBCbyblock(message):
    global iv,key
    plaintext=b''
    raw = b64decode(message)
    n=16 # size of 1 block
    blocks=[raw[i:i+n] for i in range(0,len(raw),n)]
    priv=iv
    for i in range(0,len(blocks)-1):
        block=blocks[i]
        cipher = AES.new(key, AES.MODE_CBC, priv)
        pt = cipher.decrypt(block)
        plaintext+=pt
        priv=block
    #last block
    priv=blocks[-2]
    lastblock=blocks[-1]
    cipher = AES.new(key, AES.MODE_CBC, priv)
    pt = unpad(cipher.decrypt(lastblock), 16)
    return plaintext+pt
def decrypt(message):
    try:
        global iv,key
        raw = b64decode(message)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(raw), 16)
        print (pt)
    except ValueError:
        print("Incorrect decryption")
def encrypt(message):
    global iv,key
    cipher = AES.new(key, AES.MODE_CBC,iv)
    ct_bytes = cipher.encrypt(pad(message, 16))
    ct = b64encode(ct_bytes).decode('utf-8')
    return ct 

c=encrypt(b'secddddddddddddddddddddddddddddddddddddddddddrect')
print(c)
encryptCBCbyblock(b'secddddddddddddddddddddddddddddddddddddddddddrect')
print(decryptCBCbyblock(b'ehkulw7HOq0+Q4MhlMFHaeEeFaR8x4lzq3KPRJ0jzKTQuT+hcsySW4KWJdQ0pyzw9H1bDMDSalR0uZFpzLsz5g=='))
decrypt(c)
#f=open("10.txt","r")
#for line in f:
#    res=encryptCBCbyblock(line)
#    decryptCBCbyblock(res)

