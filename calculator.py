def basic():
    cops = 0
    print("""
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -   
    -
    -
    -
    -
    -
    -  
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -   
    -
    -
    -
    -
    -
    -
    ---------------------------------------------------------------------------------
    -                                      :                                        -
    -                 +                    :              -                         -
    -                                      :                                        -
    ---------------------------------------------------------------------------------
    -                 X                    :                                        -
    -                 x                    :                /                       -
    -                 *                    :                                        -
    ---------------------------------------------------------------------------------
    """)
    if cops >=1:
        print (result)
    mode = input("Please select a mode: ")
    print("")
    print("")
    print("")
    num1 = int(input("Inrtoduct the first number of the operation: "))
    num2 = int(input("Inrtoduct the second number of the operation: "))
    if mode == "+":
        result = num1 + num2
    elif mode == "-":
        result = num1 - num2
    elif mode == "*" or "x":
        result = num1 * num2
    elif mode == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("you can't (*)for ZERO")
    else:
        print("number not found")
    print("")
    print("")
    print("")
    print(result)
    cops = cops + 1
while True:
    basic()
