# thay đổi role user thành admin
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import random
import os


def encrypt(message):
    global key
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(message,16))
    return ct_bytes.hex()
def decrypt(enc):
    global key
    enc = bytes.fromhex(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(enc),16).decode('utf8')
def profile_for(email):
    if b'&'in email or b'=' in email:
        return False
    print(encrypt(b"email="+email+b"&uid=10&role=user"))
    #print(b"email="+email+b"&uid=10&role=admin")
def parse(strs):
    arr=strs.split('&')
    re={}
    for x in arr:
        arr1=x.split('=')
        re.update({arr1[0]: arr1[1]})
    return re

key=b'keyisverysecures'
#print(parse(b'a=1&b=2'))
profile_for(b'nht@gmail.com')

# email=nht@gmail. com&uid=10&role= user
#
# block 1 ea9bdeaabe30226253e0d6f62eccc280 email=nht@gmail.
# block 2 6272671b2afc5298722150398fab1100 com&uid=10&role=
# block 3 6534d200d13e4e8ef6153aae11ccdea7 user

# email=nht@gmail. com&uid=10&role= admin
#
# block 1 ea9bdeaabe30226253e0d6f62eccc280 email=nht@gmail.
# block 2 6272671b2afc5298722150398fab1100 com&uid=10&role=
# block 3 2748689007c8921e301fcfec3fa86aa3 admin

# be admin?
# block 1 ea9bdeaabe30226253e0d6f62eccc280 email=nht@gmail.
# block 2 6272671b2afc5298722150398fab1100 com&uid=10&role=
# block 3 2748689007c8921e301fcfec3fa86aa3 admin


print(parse(decrypt('ea9bdeaabe30226253e0d6f62eccc2806272671b2afc5298722150398fab11002748689007c8921e301fcfec3fa86aa3')))
