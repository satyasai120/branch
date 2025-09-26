#factorial sum

# num=int(input("give the number:"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

#FS 3

# x=int(input("give the number:"))
# y=int(input("give me number:"))
# z=x*y
# if x!=y:
#      print("not square")
# else:
#      print(z)

#FS 4
# num1=int(input("give the number:"))
# root=num1*0.5
# if root==int(root):
#     print("perfect square")
# else:
#     print("not")

#FS 5
# num1=int(input("give the number:"))
# root=num1+1
# if root==int(root):
#     print("sunny")
# else:
#     print("not")

#FS 6
# x=int(input("give num:"))
# root=x**2
# sum=0
# while root>0:
#     digit=root%10
#     sum+=digit
#     root=root//10
# if sum==x:
#     print("neon")
# else:
#     print("not neon")

# harshad FS
# num1=int(input('num:'))
# temp=num1
# sum=0
# while num1>0:
#     digit=num1%10
#     sum+=digit
#     num1//=10

# if temp%sum==0:
#     print("harshad")
# else:
#     print("not")

#automrophic number
def is_automorphic(number):
   square = number ** 2
   mod = 10 ** len(str(number))
   if square % mod == number:
       print("It's an Automorphic Number")
   else:
       print("It's not an Automorphic Number")










    
