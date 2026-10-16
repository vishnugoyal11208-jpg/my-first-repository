# d={1:"Ram",2:"Suresh",3:"Mahesh"}
# if 2 in d:
#     print(d[2])
# else:
#     print("key not found")

# d={}
# n=int(input("Enter number of employees:"))
# i=1
# while i<=n:
#     name=input("Enter Employee Name:")
#     salary=float(input())
#     d[name]=salary
#     i=i+1
# for x in d:
#     print("The name is:",x,"and his salary is",d[x])

# d={1:"Ramesh",2:"suresh",3:"mahesh"}
# print("Before deleting key from dictionary:",d)
# del d[1]
# print("after deleting key from dictionary:",d)

d={1:"amit",2:"ramesh",3:"suresh"}
# print(d.get(1))
# print(d.get(100,"key not found"))
# print(d.pop(1))
# print(d)
# d.popitem()
# print(d)
for k, v in d.items():
    print(k,"---",v)
l1=[1,2,3,4,5,6,7,8,9]
d={i:i**2 for i in l1}
print(d)