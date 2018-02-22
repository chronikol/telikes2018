memory=[]
for i in range(30000):
	memory.append(0)
file=open("fuck.txt","r")
contents=file.read()
a=list(contents)
a.append("end")
mp=0
tp=0
while (a[tp]!='end'):
	if (a[tp]=="<"):
		mp=mp-1
	elif (a[tp]==">"):
		mp=mp+1
	elif (a[tp]=="+"):
		memory[mp]=memory[mp]+1
	elif (a[tp]=="-"):
		memory[mp]=memory[mp]-1
	elif (a[tp]=="."):
		print chr(memory[mp]),
	elif (a[tp]==","):
		memory[mp]=ord(input())
	elif (a[tp]=="["):
		if (memory[mp]==0):
			out=1
			while (out>0):
				tp=tp+1
				if (a[tp]=="]"):
					out=out-1
				elif (a[tp]=="["):
					out=out+1
	elif (a[tp]=="]"):
		out=1
		while (out>0):
			tp=tp-1
			if (a[tp]=="]"):
				out=out+1
			elif (a[tp]=="["):
				out=out-1
		tp=tp-1
	tp=tp+1
	#print memory[0]
