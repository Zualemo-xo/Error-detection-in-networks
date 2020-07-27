size=int(input("Enter the number of hexadecimal words:"))
print("Enter the hexadecimal numbers:")
lhexadecimal,lbinary,lt=[],[],[]
#Hexadecimal to binary conversion

for i in range(0,size):
    hd=input()
    lhexadecimal.append(hd)
    binaryb= "{0:08b}".format(int(hd, 16))
    lbinary.append(binaryb)
    lt.append(binaryb)
binary=''.join(lt)
print("The binary form is:",binary)
#print("Separately:",lbinary)

#Checksum for 16 bit
print(lbinary[0][0])
carry=[]
addition=[]
for i in range(len(list(str(lbinary[0])))-1,-1,-1):#Starts from last digit to MSB for addition
    cnt=0
    for j in range(0,len(lbinary)):#To add each set of binary values
        if(int(lbinary[j][i])==1):
            cnt+=1
    cnt+=len(carry)
    #print(cnt)
    carry=[]
    carry=[1]*(cnt//2)
    #print(carry)
    addition.append(cnt%2)
#addition.append(''.join(carry))
#carry consists only of 1
    #addition.append(carry[i])
cnt=0
cnt=len(carry)
    #print
tt=[0]*(cnt//2)
for i in range(0,len(tt)):
    addition.append(0)
if((cnt%2)==0):
    addition.append(1)
addition.reverse()
#print(''.join(carry))
#print(''.join(addition))
ls=[]
print("The sum:")
for i in addition:
    print(i,end='')#number after addition
    ls.append(str(i))
print('')
#for adding extra carries

#t1=addition[len(carry):]
#carry=addition[:len(carry)]
sum=''.join(ls[len(carry):])
carry=''.join(ls[:len(carry)])
sum = bin(int(sum,2) + int(carry,2))
sum=sum[2:]
print("After removing overflow digits:",sum)
print("The one's complement and the part to be encoded is:")
for i in sum:
    if(int(i)==0):
        print(1,end='')
        lt.append('1')
    else:
        print(0,end='')
        lt.append('0')
print()
print("The final encoded message is:",''.join(lt))
#code for screenshot 1 ends here

#module added to check at the reciever (For screenshot 2 and 3)
chk=input("Enter the message recieved:")
if(chk==''.join(lt)):
    print("Same message recieved")
else:
    print("Error in transmission")
