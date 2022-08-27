# a=['simple', 'is', 'better', 'than','complex']
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#     i+=1
# print(max)
    

# l=[6,1,3,5,6,3,2]
# i=0
# a=[]
# while i<len(l):
#     if l[i]not in a:
#         a.append(l[i])
#     i+=1
# print(a)
# j=0
# sum=0
# b=0
# while j<len(l):
#     sum=l[j]*l[j]
#     b=sum+b
#     j+=1
# print(b)


a={'a':1,'b':2,'c':3}
b=a.values()
c=a.keys()
d=list(b)
f=list(c)
e=[]
i=0
while i<len(b):
    n=[f[i],d[i]]
    e.append(n)
    i=i+1
print(e)
    