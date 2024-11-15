def bonjour():
    x="Bonjour"+"A3"
    print(x)

# test
bonjour()

def bonjour():
    x="Bonjour"+"A3"
    return(x)

# test
bonjour()

def bonjour(arg1, arg2):
    x = "Bonjour" + arg1 + arg2
    print(x)

# test
bonjour("A3","TP3")

def bonjour(arg):
    x = "Bonjour " + arg
    return(x)

# test
y = " TP3"
res = bonjour("A3")
print(res + y )