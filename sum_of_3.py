# main.py

def sum_of_three_numbers(num1, num2, num3):
    return num1 + num2 + num3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = sum_of_three_numbers(num1, num2, num3)

print(f"The sum of {num1}, {num2}, and {num3} is {result}")
