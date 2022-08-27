dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic1:
    if i in dic2:
        dic2[i]=dic1[i]+dic2[i]
dic1.update(dic2)
dic1.update(dic3)
print(dic1)




# d1={'a':200,'b':100,'c':300}
# d2={'a':300,'b':200,'d':400}
# dict1={}
# n=list(d1)
# m=list(d2)
# i=0
# while i<len(n):
#     if n[i] in m[i]:
#         dict1[n[i]]=d1[n[i]]+d2[m[i]]
#     else:
#         dict1[n[i]]=n[i]=d1[n[i]]
#         dict1[m[i]]=m[i]=d2[m[i]]
#     i+=1
# print(dict1)













































