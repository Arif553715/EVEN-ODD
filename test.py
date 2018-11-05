
def col(a):
    if a==1:
        n=int(input("enter a number: "))
        if n%2==0:
            print("number", n, "is Even")
            return col(1)
        else:
            print("number", n, "is Odd")
            return col(1)


col(1)