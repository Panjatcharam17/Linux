x = "global"  # Global Scope

def outer():
    x = "enclosing"  # Enclosing Scope
    def inner():
        x = "local"  # Local Scope
        print(x)
    inner()
    print(x) 

outer()
print(x)
