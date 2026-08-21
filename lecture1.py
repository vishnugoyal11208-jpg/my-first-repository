print("Hello world")

a = "Amit"
a = bool(a)
print(type(a))
print(a*234)
print(a+5)

b = ""
b = bool(b)
print(b)
print(b*5 + 4)

print(a + b)

z = ''' This is a mutli line string. 
i sjiefhofiofo
'''
print(z)

a = "hello eveyone this is the first lecture of python programming"
print(a)


# we can only store whole numbers and no. in range(0, 256) in bytes data type.

x= [12,42,53,75,97]
y = bytes(x)
#print(y[0])
#rint(y[1])
#print(y[2])
#print(y[3])
#print(y[4])

for i in y:
    print(i)

a = range(1, 11)

for i in a:
    print(i)

a = range(1, 11, 3)

for i in a:
    print(i)
    
