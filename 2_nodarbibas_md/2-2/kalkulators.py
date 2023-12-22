import calc
import sys

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
    try:
        num1 = float(sys.argv[0])
        num2 = float(sys.argv[2])
        operation = sys.arg[1]

        result = calculation(num1, num2, operation)

        print(result)
    except(ValueError, IndexError):
        print("Kaut kas nesagaja :(")

    