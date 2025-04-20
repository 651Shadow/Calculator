def isNumber(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def plus(num1,num2):
    output = float(num1) + float(num2)
    return output

def minus(num1,num2):
    output = float(num1) - float(num2)
    return output

def divide(num1,num2):
    output = float(num1) / float(num2)
    return output

def multiply(num1,num2):
    output = float(num1) * float(num2)
    return output

def inputs():
    num1 = input ("Input your first number or 'q' to quit: ")
    while not isNumber(num1):
        if num1 == ("q"):
            exit()
        print("Error, please enter a valid number")
        num1 = input("Input your first number: ")
    print("Choose your sign: (+, -, /, X) 1-4 ")
    sign_inp = ( 
        "(+ is 1) " 
        "(- is 2) " 
        "(/ is 3) "
        "(X is 4) " )
    sign = input( sign_inp)
    num2 = input("Input your second number:")
    while not isNumber(num2):
        print("Error, please enter a valid number")
        num2 = input("Input your second number: ")
    return num1,num2,sign

while True:
    num1,num2,sign = inputs()

    if sign == ('+') or sign == ("1"):
        print(plus(num1,num2))
    elif sign == ("-") or sign == ("2"):
        print(minus(num1,num2))
    elif sign == ("/") or sign == ("3"):
        print(divide(num1,num2))
    elif sign in ["X", "x", "*"] or sign == ("4"):
        print(multiply(num1,num2))
    else:
        print("Error, Restart....")