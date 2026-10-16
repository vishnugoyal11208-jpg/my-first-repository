
# num=int(input())
# for i in range(1,11):
#     print(f"{num}X{i}={num*i}")
#     if i==6:
#         break

# str=input()
# vowels=["a","e","i","o","u"]
# no_of_vowels=0
# for i in str:
#     if i.lower() in vowels:
#         no_of_vowels+=1
# print(no_of_vowels)
# str="1,2,3,4,5,6,7,8,9"
# l=str.split(",")
# print(l)
# print(type(l))

# str=input()
# list=str.split(" ")
# new_list=[]
# for item in list:
#     if item in new_list:
#         continue
#     else:
#         new_list.append(item)
# new_list.sort()
# print(new_list)

# a=int(input())
# b=int(input())
# print(f"Before swapping:a={a},b={b}")
# t=a,b
# b,a=t
# print(f"After swapping:a={a},b={b}")

# n=int(input())
# dic={}
# max_marks=0
# sum=0
# for i in range(n):
#     name=input()
#     marks=int(input())
#     dic[name]=marks
#     sum+=marks
#     if marks>=max_marks:
#         max_marks=marks
#         Topper=name

# print(f"Topper:{Topper} with {max_marks} marks")
# print(f"Average marks:{sum/n}")


a=input()
b=input()
l1=a.split(" ")
l2=a.split(" ")
s1=set(l1)
s2=set(l2)
common_element=s1.intersection(s2)
new_list=[]
for i in s2:
    if int(i)%2==0:
        new_list.append(i**2)
print(f"Common element:{common_element}")
print(f"Square of even number:{new_list}")