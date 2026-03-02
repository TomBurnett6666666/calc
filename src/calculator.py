"""
Simple Calculator Module
Provides basic arithmetic operations
"""

class Calculator:
    """A simple calculator class"""

    def __init__(self):
        """Initialise calculator"""
        self.history = []

    def add(self, a, b):
        """Takes in 2 numbers, a and b, adds them and returns the sum as result"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Takes in 2 numbers, a and b, subtracts them and returns the difference as result"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Takes in 2 numbers, a and b, multiplies them and returns the product as result"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Takes in 2 numbers, a and b, divides them and returns the quotient as result"""
        if b == 0:
            raise ValueError("Cannot divide by 0")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result

    def get_history(self):
        """Return calculation history"""
        return self.history

    def clear_history(self):
        """Clear all calculation history"""
        self.history = []


def main():
    """Main function to run the calculator app"""
    calc = Calculator()  # create an instance of the calculator object

    print("=== Python Calculator ===")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'history' to see past calculations")
    print("Type 'quit' to exit\n")

    while True:
        operation = input("Enter operation: ").lower()

        if operation == 'quit':
            print("Goodbye!")
            break

        if operation == 'history':
            history = calc.get_history()

            if history:
                print("\n ---- Calculation History ----")
                for entry in history:
                    print(entry)
                print("-----------------------------\n")
            else:
                print("---- No history yet! ----")
            continue

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("---Invalid operation. Please enter a valid operation and try again!---")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = 0

            if operation == 'add':
                result = calc.add(num1, num2)
            elif operation == 'subtract':
                result = calc.subtract(num1, num2)
            elif operation == 'multiply':
                result = calc.multiply(num1, num2)
            elif operation == 'divide':
                result = calc.divide(num1, num2)

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Unexpected Error: {e}\n")


if __name__ == "__main__":
    main()
    