# glovar='10k coders'
# def funName():
#     glovar='python coder'
#     print(glovar)

# funName()
# print(glovar)

# satya='jobless'
# def funN():
#     satya='aspiring'
#     print(satya)

# funN()
# print(satya)

#enclosing and local name
# def outer():
#     var1='satya'
    
#     def inner():
#         nonlocal var1
#         var1='student'
#         print(var1)
#     print(var1)
#     inner()
# outer()
var1="created"
def outer():
    global var1
    var1='created'
    def inner():
        var1='resume'
        print(var1)
    def local():
        var1='create'
        print(var1)
    local()
    inner()
    print(var1)
outer()
