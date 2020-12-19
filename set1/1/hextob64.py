#set 1 HEX to BASE64

import base64
import codecs

str="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64 = codecs.encode(codecs.decode(str, 'hex'), 'base64').decode('utf-8')
print (b64)
