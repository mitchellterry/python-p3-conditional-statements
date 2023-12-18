#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'ADMIN') or (username == 'admin') and password == '12345':
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    response = ""
    if temperature < 40:
        response = "brisk"
    elif 40 <=temperature<= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"
    # your code here
    pass

def fizzbuzz(num):
    
    if(num %3 == 0) and (num %5 == 0):
        return "FizzBuzz"
    elif(num %3 == 0):
        return "Fizz"
    elif(num %5 == 0):
        return "Buzz"
    else:
        return num
    # your code here
    pass

def calculator(operation, num1, num2):
    switcher = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
    }
    result = switcher.get(operation, None)
    if result is None:
        print("Invalid operation!")
    return result    
    # your code here
    # if operation == '+':
    #     return num1 + num2
    # elif operation == '-':
    #     return num1 - num2
    # elif operation == '*':
    #     return num1 * num2
    # elif operation == '/':
    #     return num1 / num2
    # else:
    #     print("Invalid operation!")
    #     return None
    pass
