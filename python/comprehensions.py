#list comprehension
# list1=[1,2,3,4,5]

#create an list which contains squares of each element in the above list

# squares=[i**2 for i in list1]
# print(squares)

# list1=list(range(1,11))
# odds=[x for x in list1 if x%2!=0]
# print(odds)

#tuple comprehension
# celsius=(45,90,60,89)
# farenheit=tuple((9/5)*temp +32 for temp in celsius)
# print(farenheit)

# tuple1=('satya','siddu','ganesh','mani')
# far=tuple(i[0] for i in tuple1)
# print(far)

# num=('satyasai','ganesh bavu','siddu','mani')
# num1={x for x in num if len(x)>5}
# print(num1)

# list1=[4,5,7,9,2,56,34,2,4,8]

# set1={i**3 for i in list1}
# print(set1)
# list1=['satyasai','siddu','maniteja','ganesh']
# dict1={name:len(name) for name in list1}
# print(dict1)
# dict2={value:key for key, value in dict1.items()}
# print(dict2)

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
list1=[num for row in matrix for num in row]
print(list1)