#set 1 SIGNLE-BYTE XOR CIPHER

import string 
#cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

cipher="706a757a6b806a3a3c7d726a75316d7b797c457275746d48867d795b4d947f984480849c83929f869b5a6e5ea9"
def xor(string,ch):
    string_bytes = bytes.fromhex(string)
    return "".join([chr(a0 ^ ord(ch)) for a0 in string_bytes]) 

if __name__ == "__main__":
    alphabeta = string.ascii_letters + string.digits 
    for ch in alphabeta : 
        print(xor(cipher,ch))  
        ''' find meaning word ''' 

