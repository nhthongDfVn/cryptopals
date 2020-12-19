# ý tưởng là lọc mỗi 32 bit và kiểm tra xem có block nào giống nhau không

f=open("8.txt","r")
n = 32
for line in f:
    line=line.strip()
    arr=[line[i:i+n] for i in range(0,len(line),n)]
    myset=set(arr)
    if len(arr)!=len(myset):
        print ("[+] We find it: " + line)
