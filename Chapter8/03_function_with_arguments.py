def goodDay(name, ending):
    print("Good Day, ",name)
    print(ending)

goodDay("Harry", "Thank you")
goodDay(90, "O bytes")
goodDay("Sandip", "Thank you very much")

def badDay(name, ending):
    print("Good Day, "+name)
    print(ending)
    return "done"

a = badDay("Sandip", "Thank you very much")
print(a)


