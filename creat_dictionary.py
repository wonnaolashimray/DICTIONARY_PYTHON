# i=0
# a=[]
# while i<15:
#     user=int(input("enter the number"))
#     a.append(user)
#     i+=1
# print(a)
# j=0
# c={}
# while j<len(a):
#     c[a[j]]=a[j]*a[j]
#     j+=1
# print(c)



list1=[[1,2,4,8,10],[1,4,15,11],[10,20,30,40,50,60]]
i=0
l=[]
while i<len(list1):
    j=0
    sum=0
    while j<len(list1[i]):
        sum=sum+list1[j]
        j+=1
        # sum+=s
    # l.append(sum)
    i+=1
print(sum)

