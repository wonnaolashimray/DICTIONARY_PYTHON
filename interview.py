# x=12
# for i in range(5):
#     x=x-2
#     print(x)


# a={'a':1,'b':2,'c':3}
# l=[]
# for i in a:
#     if i in a:
#         b=[]
#         b.append(i)
#         b.append(a[i])
#     l.append(b)
# print(l) 



a=[[4,2,1],[3,2,6],[9,8]]
# O/P=[1,6,8]
i=0
e=[]
while i<len(a):
    j=-1
    while j<len(a[i])-1:
        e.append(a[i][j])
        j=j-1
        break
    i=i+1
print(e)



a=[[4,2,1],[3,2,6],[9,8]]
#O/P=[1,6,8]
list=[]
for i in range(len(a)):
   for j in range(len(a)):
      n=a[i][-1:]
      list+=n
      break
print(list)


a=[[4,2,1],[3,2,6],[9,8]]
#O/P=[1,6,8]
list=[]
i=0
while i<len(a):
   j=0
   while i<len(a):
      n=a[i][-1:]
      list+=n
      i+=1
      j+=1
print(list)

