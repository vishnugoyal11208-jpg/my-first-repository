# x="PROGRAMMING"
# print(f"Odd string: {x[0::2]}")
# print(f"even string:{x[1::2]}")

# s = "DATASCIENCE"

# substring=s[2:7]
# print(substring)
# list=[]
# for i in range(1,6):
#     list.append(s[7-i])
# x="".join(list)
# print(x)

str=input("Enter the string:")
print(str[0:3])
print(str[len(str):len(str)-4:-1])
print(str[2:7])
print(str[::2])
print(str[len(str)::-1])