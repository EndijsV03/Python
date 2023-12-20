import calc

def parseInput(inputStr):
    inputList = inputStr.split()

    num1 = float(inputList[0])
    num2 = float(inputList[2])

    operation = inputList[1]

    return num1, num2, operation

def calculation(num1, num2, operation):
    if operation == "+":
        result = calc.summa(num1, num2)
    elif operation == "-":
        result = calc.atnemsana(num1, num2)
    elif operation == "/":
        result = calc.dalisana(num1, num2)
    elif operation == "*":
        result =calc.multiplikacija(num1, num2)
    elif operation == "^":
        result = calc.eksponenta(num1, num2)
    else:
        result = "Nepareizs operators"
    
    return result

if __name__ == "__main__":
    userInput = input('Ievadiet operaciju: ')

    try:
        num1, num2, operation = parseInput(userInput)
        result = calculation(num1, num2, operation)

        print(result)
    except(ValueError, IndexError):
        print("Kaut kas nesagaja :(")

    