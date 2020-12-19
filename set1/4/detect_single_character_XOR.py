#set 1 DETECT SINGLE-CHARATER XOR CIPHER

import string 

def xor(string,ch):
    string_bytes = bytes.fromhex(string)
    return "".join([chr(a0 ^ ord(ch)) for a0 in string_bytes]) 
def check(string1):
    for index in string1:
        if index not in string.printable:
            return False
    return True
if __name__ == "__main__":
    alphabeta = string.ascii_letters + string.digits
    num=0
    f=open("detect.txt","r")
    for cipher in f:
        num+=1
        #print ("[+]=================================================================[+]<<" +str(num))
        for ch in alphabeta : 
            if check(xor(cipher,ch))==True:
                print(xor(cipher,ch))
    print("Finish!!")
