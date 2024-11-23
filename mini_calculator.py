def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiple(a,b):
    return a*b

def calculator(condition,a,b):
    if condition == '+':
        return add(a,b)
    elif condition == '-':
        return sub(a,b)
    elif condition == '*':
        return multiple(a,b)
    else:
        return ' invalid'

a= int(input('enter'))
b= int(input('enter'))
condition= input('enter the operation')

result = calculator(condition,a,b)
print(result)

