def credit(times1):
  c=int(a.readline())
  l=int(a.readline())
  i=map(int,a.readline().split())
  b=list(i)
  b.sort()
  ri=len(i)-1
  li=0
  o=[]
  while li<ri:
    if b[li]+b[ri]==c :
      for num in range(0,l):
        if(i[num]==b[li] or i[num]==b[ri]):
          o.append(num)
      o.sort()
      f.write("Case #{}: {} {}".format(times1+1,o[0]+1,o[1]+1))
      f.write("\n");
      break
    elif(b[li]+b[ri]<c):
      li+=1
    else:
      ri-=1



if __name__ == '__main__':
  a=open('in.txt','r')
  f=open('out.txt','w')
  for times in range(0,int(a.readline())):
    credit(times)
  a.close()
  f.close()
