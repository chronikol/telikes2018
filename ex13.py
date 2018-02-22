n=input("dose n")
while (n>9):
	print "the number must be <=9!"
	n=input("dose n")
l=[]
for i in range(n+2):
    l.append(i)
l[n+1]=10
#print l#svisto!
s=input("dose s")
total=0
su=0
p=n


while (p!=0):
	p=n

	while (l[p]+1!=l[p+1]):
	        for i in range(1,n+1):#check
			su=su+l[i]
			#print "su", su #svisto
		if (su==s):
			total=total+1
			#print "=====",l,"=====" #svisto
		su=0
	        l[p]=l[p]+1
		#print l #svisto
	while (l[p]==l[p+1]-1):# metakini ton p mia thesi piso
	        p=p-1
		#print "p=", p
		l[p]=l[p]+1
		if (p==0):
			#print l#svisto
			for i in range(1,n+1):#check
				su=su+l[i]
				#print "su", su#svisto
			if (su==s):
				total=total+1
				#print "=====",l,"====="#svisto
			su=0
	for i in range(p,n):# midenizi tous epomenous
	        l[i+1]=l[i]+1
		#print l#svisto
	
print total
