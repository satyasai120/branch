# def funcName():
#     msg='hello' #local variable / local scope
#     print(msg)

# funcName()
# print(msg)

# var1='gobal' #global variables
# def glocheck():
#     print(var1)

# glocheck()

# var1='ande' #task1
# def globalvar():
#     var2='satyasai'
#     print(var2,var1) 

# globalvar()

#task2
# emplo='tester'
# def devlop():
#     position='manager'
#     emplo='analyst'
#     print(emplo)
#     print(position)

# devlop()
# print(emplo)

# num1=10
# def tharuniBday():
#     global num1 #here i am delcaring num1 as aglobal variable
#     num1=num1+1
#     print(num1)

# tharuniBday()
# print(num1)

x='hello'
def insidefunction():
    global x
    x+=' world'
    print(x)

insidefunction()


