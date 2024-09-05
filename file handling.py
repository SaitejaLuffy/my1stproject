f= open("C:\\Users\\ASUS\\Documents\\configuration-Office365-x64.txt",'r')
#f.write("saiteja bekkam")
#f.write("ME-PSPE")
print(f.read())

f1=open("C:\\Users\\ASUS\\Documents\\My Documents\\IMG-20220719-WA0009.jpg",'rb')
f2=open("mypic.jpg",'wb')
for i in f1:
    f2.write(i)

print(f1.read())