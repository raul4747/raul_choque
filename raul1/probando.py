x="siempre luchare"
c1=0
c2=0
c3=0
c4=0
c5=0
for i in range(0,len(x)):
    if x[i]=="a":
        c1+=1
    if x[i]=="e":
        c2+=1
    if x[i]=="i":
        c3+=1
    if x[i]=="o":
        c4+=1
    if x[i]=="u":
        c5+=1
print ("la vocal a se repite",c1,"veces")
print ("la vocal a se repite",c2,"veces")
print ("la vocal a se repite",c3,"veces")
print ("la vocal a se repite",c4,"veces")
print ("la vocal a se repite",c5,"veces")