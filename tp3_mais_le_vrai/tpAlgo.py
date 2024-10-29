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

def bonjour(arg):
    x = "Bonjour" + arg
    print(x)

# test
bonjour("A3")

def bonjour(arg):
    x = "Bonjour" + arg
    return(x)

# test
res = bonjour("A3")
print(res)