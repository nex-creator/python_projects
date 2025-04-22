import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations= {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is first number?"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("pick the operations:")
        num2 = float(input("what is the next number."))
        answer = operations[operations_symbol](num1, num2)
        print(f" {num1} {operations_symbol} {num2} = {answer}")
        choice = input(f" Type 'y' to continue calculating with {answer},"
                       f"or type 'n' to start new calculation:\n").lower()
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()