from src.main import Calculator
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple command-line calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="the arithmetic operation to perform")
    parser.add_argument("x", type=float, help="the first operand")
    parser.add_argument("y", type=float, help="the second operand")

    args = parser.parse_args()

    calculator = Calculator()

    if args.operation == "add":
        result = calculator.add(args.x, args.y)
    elif args.operation == "subtract":
        result = calculator.subtract(args.x, args.y)
    elif args.operation == "multiply":
        result = calculator.multiply(args.x, args.y)
    elif args.operation == "divide":
        result = calculator.divide(args.x, args.y)

    print(result)
