def base(time):
    text=fin.readline().rstrip('\n')
    b=[]
    for i in xrange(2,37):
        try:
            a=int(text,i)
            for j in xrange(2,37):
                try:
                    c=int(str(a),10)
                    b.append(c)
                except ValueError:
                    pass
        except ValueError:
            pass
    b.sort()
    print b
    fout.write("Case #{}: {}\n".format(time+1,b[0]))
if __name__ == '__main__':
    fin=open('in.txt','r')
    fout=open('out.txt','w')
    for time in xrange(0,int(fin.readline().rstrip('\n'))):
        base(time)