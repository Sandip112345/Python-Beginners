# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)

# finally:
#     print("I am inside finally statement.")

# why we use finally


def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return

    # else: # Here the else stattement would not be called because of return in try and except
    #     print("I am inside finally statement.")

    finally: # but finally would be printed even if there is return function, it will preside over it.
        print("I am inside finally statement.")

main()
    