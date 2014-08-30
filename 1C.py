#!/usr/bin/env python
def vecmul(time):
    vecnum=int(fin.readline())
    x=map(int,fin.readline().split())
    print x
    x.sort(reverse=True)
    y=map(int,fin.readline().split())
    y.sort()
    z=[x[i]*y[i] for i in xrange(0,vecnum)]
    a1=0
    for item in z:
        a1+=item
    fout.write("Case #{}: {} \n".format(time+1,a1))
if __name__ == '__main__':
    fin=open('in.txt','r')
    fout=open('out.txt','w')
    for time in xrange(int(fin.readline())):
        vecmul(time)
    fin.close()
    fout.close()