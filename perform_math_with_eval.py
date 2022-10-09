def add(a, b):
    print("Add function executed", a+b)
    return a + b


def sub(a, b):
    print("Sub function executed", a - b)
    return a - b


def mul(a, b):
    print("Mul function executed", a * b)
    return a*b


def div(a, b):
    if a==0 or b==0:
        print("Div function executed", 0)
        return 0
    print("Div function executed", a/b)
    return a/b
    
def perform_math_with_eval(a, b, func_symbol):

    switcher = {
        '+': 'add(a, b)',
        '-': 'sub(a, b)',
        '*': 'mul(a, b)',
        "/" : 'div(a, b)'
    }

    func = switcher.get(func_symbol, 0)
    print(f"Result found for operation:'{func_symbol}' for values {a} and {b} is", eval(func))


print()
print('-----------------------------------------------------------------------')
print('Code execution with the help of eval')
print('-----------------------------------------------------------------------')
perform_math_with_eval(9, 3, "+")
print('-----------------------------------------------------------------------')