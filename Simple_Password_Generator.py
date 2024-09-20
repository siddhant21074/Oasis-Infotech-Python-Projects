import random

''' 
    Defining  the variables with proper and required data
'''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=",
                   "[", "]", "{", "}", "|", "/", "<", ">", ".", ",", "?", "/",
                   "'", '"', "`", "~"]

'''
    Taking input from user about number of each characters present in the password
'''

num_of_letter = int(input("Choose the number of letters : "))
num_of_symbols = int(input("Choose the number of symbols : "))
num_of_numbers = int(input("Choose the number of numbers : "))

'''
    Defining the separate function 
'''


def letters_function(num_of_letters1):
    new_list = []
    for i in range(num_of_letters1):
        var = random.choice(letters)
        new_list.append(var)
    return new_list


def symbols_function(num_of_symbols1):
    new_list = []
    for i in range(num_of_symbols1):
        var = random.choice(special_symbols)
        new_list.append(var)
    return new_list


def numbers_function(num_of_numbers1):
    new_list = []
    for i in range(num_of_numbers1):
        var = random.choice(numbers)
        new_list.append(var)
    return new_list


'''
    Storing the result and performing the operations
'''
separator = ""

result1 = letters_function(num_of_letter)
random.shuffle(result1)
s1 = separator.join(result1)

result2 = symbols_function(num_of_symbols)
random.shuffle(result2)
s2 = separator.join(result2)

result3 = numbers_function(num_of_numbers)
random.shuffle(result3)
s3 = separator.join(result3)

'''
    Concat the strings and display result
'''
sample = (s1 + s2 + s3)
print(f'Your Password is: {sample}')
