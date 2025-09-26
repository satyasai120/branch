# def addition(*numbers):
#     add=0
#     for i in numbers:
#         add+=1
#         return add
#     print(addition(1,2,3,4,5))

# def mutlipication(*numbers):
#     mutlipication*1
#     for i in numbers:
#         add*=1
#         return add
#     print(mutlipication(11,4,56))

# def details(** adhaarinfo):
#     for i,j in adhaarinfo.items():
#         print(f'{i}:{j}')
#         print("not verified")
#         return print(" adhaar verified")

# details(name="satya" , age="22" , place="hyderabad")
# details(name="sai", age="22" , place="hyd")
# details(name="siddu" , age="22" , place="hyd")

# def details(model,year):
#     print(f"your car model is {model} and year is {year}")

# details(model='car',year="2023")

# def variable(*numbers,):
#     add=0,multipication==+i
#     for i,j in numbers:
#          add+=1,multipication*1==i
#     return add
    
# print(variable(1,34,56))
# print(variable(2,34,56))

# def details(*var1,**var2):
#     for i in var1:
#         print(i)
#     for j,k in var2.items():
#         print(f"{j}:{k}")

# details(1,2,3,4, name="satya" , age="22")

# def funcname(*var1,**var2):
#     add+i=0
#     mult*j=0
#     for i,j in var1.items():
#         return var1
#     sub-k=0
#     div%l=0
#     for k,l in var2.items():
#         return var2
    
# print(funcname(1,2,3,6,7))


def computations(a,b):
    return a+b,a-b,a*b,a/b

add, sub, mul, div=computations(10,20)
print(add,sub,mul,div)