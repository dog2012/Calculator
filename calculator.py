def basic():
    print("Modes:")
    print("(1)sum")
    print("(2)res")
    print("(3)mul")
    print("(4)div")
    mode = input("Please select a mode: ")
    num1 = int(input("Inrtoduct the first number of the operation: "))
    num2 = int(input("Inrtoduct the second number of the operation: "))
    if mode == "1":
        result = num1 + num2
    elif mode == "2":
        result = num1 - num2
    elif mode == "3":
        result = num1 * num2
    elif mode == "4":
        if num2 != 0:
            result = num1 / num2
        else:
            print("you can't (*)for ZERO")
    else:
        print("number not found")
    print(result)
basic()