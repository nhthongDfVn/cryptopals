#set 1 Fixed XOR

import base64
import codecs

str1="1c0111001f010100061a024b53535009181c"
str2="686974207468652062756c6c277320657965"
re=""

for i in range(0,len(str1),2):
    s1=str1[i]+str1[i+1]
    s2=str2[i]+str2[i+1]
    re=re+ hex(ord(codecs.decode(s1,'hex'))^ord(codecs.decode(s2,'hex')))[2:]
print (re)
