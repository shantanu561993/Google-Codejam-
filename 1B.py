def reverse(times):
    c=a.readline().split()
    d=[c[i] for i in range(len(c)-1,-1,-1)]
    b.write("Case #{}: ".format(times+1))
    for item in d:
        b.write("{} ".format(item))
    b.write("\n")
if __name__ == '__main__':
    a=open('in.txt','r');
    b=open('out.txt','w')
    for time in xrange(0,int(a.readline())):
        reverse(time)
    a.close()
    b.close()