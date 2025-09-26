# def add1(a,b):
#     return a+b
# print(add1(5,10))

# add1=lambda a,b: a+b
# print(add1(5,10))

#write a lambda function to find square of a number

# sql=lambda x:x*x
# print(sql(5))

# even_odd=lambda num1: 'even' if num1%2==0 else 'odd'
# print(even_odd(25))

#map
# list1=[1,2,3,4,5]
# squares=list(map(lambda x:x*x*3, list1))
# print(squares)

#sort()
# list1=[2,5,4,3,6,9]
# list1.sort(key=lambda x:x)
# print(list1)
# list1=[('satya',90), ('ganesh',88), ('siddu',91), ('manitej',93)]
# dict1=dict(list1)
# print(dict1)
# sorted_dict=dict(sorted(dict1.items(), key=lambda x:x[1]))
# print(sorted_dict)

lists=[
{'name': 'satya', 'age':21},
{'name': 'ganesh', 'age':20},
{'name': 'siddu', 'age':20}
]
lists.sort(key=lambda x:x['age'])
print(lists)
# dict1=dict(lists.sort)
# print(dict1)
# sorted_name=dict(sorted(dict1.items(), key=lambda x:x))
# print(sorted_name)

# sorted_list=sorted(lists, key=lambda x:x['age'])
# print(sorted_list)