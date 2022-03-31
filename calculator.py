
firstNumber = float(input("First number: "))
secondNumber = float(input("Second number: "))

operator = input("Choose operator [+, -, * /]: ")

if operator == "+":
    print("{0} {1} {2} = {3}".format(firstNumber, operator, secondNumber, firstNumber + secondNumber))
elif operator == "-":
    print("{0} {1} {2} = {3}".format(firstNumber, operator, secondNumber, firstNumber - secondNumber))
elif operator == "*":
    print("{0} {1} {2} = {3}".format(firstNumber, operator, secondNumber, firstNumber * secondNumber))
elif operator == "/":
    print("{0} {1} {2} = {3}".format(firstNumber, operator, secondNumber, firstNumber / secondNumber))
else:
    print("Wrong input!!")

