d=[]
f=[]
counter=0
def availdir(dirs):
	global d
	c=[]
	a=dirs.split("/")
	a[0]="/"
	for i in xrange(0,len(a)-1):
		j=i-1
		if i==0:
			c.append(a[0]+a[1])
		else:
			c.append(c[j]+"/"+a[i+1])
	d=list(set(d+c))

def mkdirs(dd):
	global d
	global f
	global counter
	c=[]
	a=dd.split("/")
	a[0]="/"
	for i in xrange(0,len(a)-1):
		j=i-1
		if i==0:
			c.append(a[0]+a[1])
		else:
			c.append(c[j]+"/"+a[i+1])
	for i in xrange(0,len(c)):
		if c[i] in d:
			pass
		else:
			counter+=1
			d.append(c[i])
			
	
	
def runit(time):
	global d
	global f
	global counter
	d=[]
	f=[]
	counter=0
	a,b=map(int,fin.readline().rstrip('\n').split())
	for i in xrange(0,a):
		availdir(fin.readline().rstrip('\n'))
	
	for i in xrange(0,b):
		mkdirs(fin.readline().rstrip('\n'))
	fout.write("Case #{}: {}\n".format(time+1,counter))




	

fin=open('in.txt','r')
fout=open('out.txt','w')
for time in xrange(0,int(fin.readline().rstrip('\n'))):
	runit(time)
fin.close()
fout.close()
	
