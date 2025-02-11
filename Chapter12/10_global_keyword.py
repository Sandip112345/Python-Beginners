
a = 5

def fun():
    global a
    a = 3
    print(a)


print(f"before calling func() : a = {a}")
fun()
print(f"after calling func() : a = {a}")
    