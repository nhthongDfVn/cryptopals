import math
def _pad(text, block_size):
    """
    Performs padding on the given plaintext to ensure that it is a multiple
    of the given block_size value in the parameter. Uses the PKCS7 standard
    for performing padding.
    """
    no_of_blocks = math.ceil(len(text)/float(block_size))
    pad_value = int(no_of_blocks * block_size - len(text))

    if pad_value == 0:
        return text + chr(block_size) * block_size
    else:
        return text + chr(pad_value) * pad_value
def pad(m):
    return m+chr(16-len(m)%16)*(16-len(m)%16)
plaintext=input("Enter your plaintext: ")
print ("After add PKCS#7 ")
print (pad(plaintext).encode('utf8').hex())
print (_pad(plaintext,16).encode('utf8').hex())
