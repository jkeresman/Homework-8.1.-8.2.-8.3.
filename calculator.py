from pconst import const

const.OPERATORS = {"+", "-", "/", "*"}


def number_input():
    flag = False
    number = None

    while not flag:
        try:
            number = float(input("Enter a number: "))
            flag = True
        except ValueError as err:
            print(err)
            print("Please try again!")

    return number


def correct_operator(op):
    return op in const.OPERATORS


def operator_input():
    op = None
    while not correct_operator(op):
        op = input("Chose operation [+, -, /, *] : ")
        if not correct_operator(op):
            print("Incorrect operator, please try again!")
    return op


def multiply(num1, num2): return num1 * num2


def add(num1, num2): return num1 + num2


def subtract(num1, num2): return num1 - num2


def divide(num1, num2):
    try:
        quotient = num1 / num2
    except ZeroDivisionError as err:
        print(err)
        quotient = "Can't be divided"
    return quotient


def calculate(num1, num2, op):
    switch = {
        "+": add(num1, num2),
        "-": subtract(num1, num2),
        "*": multiply(num1, num2),
        "/": divide(num1, num2)
    }

    return switch.get(op)


first_number = number_input()
second_number = number_input()

operator = operator_input()

result = calculate(first_number, second_number, operator)

print(f"{first_number} {operator} {second_number} = " + str(result))
