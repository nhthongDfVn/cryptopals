# Finish 23/06/2020

from string import ascii_letters,digits 
import base64

strs=ascii_letters + digits + " \n!'.:?,"
f=open("6.txt","r")

def isalphabeta(string1):
    for index in string1:
        if index not in strs:
            return False
    return True
def myFunc(e):
  return e[1]
def solve():
    data=base64.b64decode(f.read())
    #print(data.decode("utf-8"))
    data=data.decode("utf-8")

    print ("[+] Find key length")
    HM_AVG=[]
    #For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
    for keysize in range (2,41):
        block=  [data[i:i+keysize] for i in range(0, len(data), keysize)]
        avg=0
        time=0
        for i in range (0,len(block)-1):
            for j in range (i+1,len(block)):
                if len(block[i])==keysize and len(block[j])==keysize:
                    time=time+1
                    avg=avg+HammingDist(block[i],block[j])
        HM_AVG.append([keysize,avg/keysize/time])
    #The KEYSIZE with the smallest normalized edit distance is probably the key. 
    HM_AVG.sort(key=myFunc)
    for i in range(len(HM_AVG)): 
        print (i, end = " ") 
        print (HM_AVG[i])
    KEY_LE=HM_AVG[0][0]
    print ("[+] Key length is : "+str(KEY_LE))

    # split block for XOR single key
    block=  [data[i:i+KEY_LE] for i in range(0, len(data), KEY_LE)]
    BlockByOne=[]
    for i in range (0,KEY_LE):
        s=''
        for j in range (0,len(block)):
            if len(block[j])==KEY_LE:
                s=s+block[j][i]
        BlockByOne.append(s)
    # single key xor
    key = []
    for i in range(0,len(BlockByOne)):
        key_i = []
        for k in strs:
            xor_string = ""
            for ch in BlockByOne[i]:
                xor_string += chr(ord(ch) ^ ord(k))
            if isalphabeta(xor_string):
                key_i.append(k) 
        key.append(key_i)
    print(key)
    
    

def HammingDist(line1, line2):
    res1 = " ".join(f"{ord(i):08b}" for i in line1)
    res2 = " ".join(f"{ord(i):08b}" for i in line2)
    count=0
    for i in range(0,len(res1)):
        if res1[i]!=res2[i]:
            count+=1
    return count
def hex_to_str(string):
    string_bytes = bytes.fromhex(string)
    return "".join([chr(a0) for a0 in string_bytes]) 
if __name__=="__main__":
    solve()
