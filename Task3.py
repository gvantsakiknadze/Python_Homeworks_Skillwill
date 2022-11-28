
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

number=int(input("Please enter the number: "))
x=factorial(number)
print(f'The factorial of {number} is {x}')
