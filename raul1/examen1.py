
#n=[1,2,3,4]
#print(sum(n))...el siguiente codigo pide el numero y calcula la suma de sus digitos
x=input("intoduzca el numero...")
#x=float(x)
r=0
for i in range(0,len(x)):
    r+=int(x[i])
print(r)