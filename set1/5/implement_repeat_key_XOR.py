import string

line='''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key='ICE'
re=''
index=0
for char in line:
    re+=chr(ord(char)^ord(key[index]))
    index=(index+1)%len(key)
print(re.encode().hex())
