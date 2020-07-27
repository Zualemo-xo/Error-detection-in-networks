#to get xor between two numbers

def xor(a,b):
    
    string=[]
    for i in range(1,len(b)):
        if(a[i]==b[i]):
            string.append('0')
        else:
            string.append('1')
    return ("".join(string))
#for the binary division

def division(dividend,divisor):
    
    l=len(divisor)
    s=dividend[0:l]
    
    while(l<len(dividend)):
        if(s[0]=='1'):
            s=xor(divisor,s)+dividend[l]
        elif(s[0]=='0'):
            s=xor('0'*l,s)+dividend[l]
        l+=1;
    if(s[0]=='1'):
        s=xor(divisor,s)
    else:
        s=xor('0'*l,s)
    c=s
    return(c)

#to encode

def encode(data,key):
    
    d=""
    k=""
    d=data+"0"*(len(key)-1)
    remainder=division(d,key)
    k=data+remainder
    print("The remainder:",remainder)
    print("The encoded data to be sent:",k)
    

pwrs=list(map(int,input("Enter the powers in the polymomial generator:").split()))
powers=[]

#for calculating polymonial power to binary

for i in range(0,max(pwrs)+1):
    if i in pwrs:
        powers.append('1')
    else:
        powers.append('0')
#print(powers)
powers.reverse()
#print(powers)
pwrs=''.join(powers)
dword=input("Enter the dataword:")
print("The binary form of the polynomial generator is:",pwrs)
encode(dword,pwrs)
