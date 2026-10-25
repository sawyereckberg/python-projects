def validate_isbn(isbn, length):
    try:
        if len(isbn) != int(length):
            print(f'ISBN-{length} code should be {length} digits long.')
            return
        main_digits = isbn[0:int(length)-1]
        given_check_digit = isbn[int(length)-1:]
        main_digits_list = [int(digit) for digit in main_digits]
    
    # Calculate the check digit from other digits
        if length == 10:
            expected_check_digit = calculate_check_digit_10(main_digits_list)
        else:
            expected_check_digit = calculate_check_digit_13(main_digits_list)
        # Check if the given check digit matches with the calculated check digit
        if given_check_digit == expected_check_digit:
            print('Valid ISBN Code.')
        else:
            print('Invalid ISBN Code.')
    except ValueError:
            print('Invalid character was found.')
        
def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
    
def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
    
def main():
    try:
        user_input = input('Enter ISBN and length: ')
        values = user_input.split(',')
        isbn = values[0]
        length = int(values[1])
        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
    except IndexError:
        print('Enter comma-seperated values.')
    except ValueError:
        print('Length must be a number.')

main()





'''
Error handling review:
Common types of error messages in Python:
1. SyntaxError: when improper syntax is used.
    Ex: print('Hello world'
    This would raise a syntax error because the parenthis isn't closed.
2. IndexError: when you're attempting to access an element outside of a given index.
    Ex: list_ex = ['one', 'two', 'three'] 
        print(list_ex[4])
    This would raise an index error since you're trying to access the 4th element, which does not exist
3. AttributeError: when you try to use a method on a data type that doesn't allow certain attributes
    Ex: num = 5 num.append('6')
    This would raise an Attribute Error because you can't append a number to an integer data type
4. NameError: when you try to access a variable that hasn't been defined yet.
    Ex: print(name) when name has never been defined will raise this error
5. TypeError: When you try to perform operations on a data type that is incapable of performing such operations
    Ex: 5 + '5'
    This would raise a TypeError because you can't add a string and integer. 

Good DeBugging Techniques in Python:
1. Use print statements often to identify what variables are doing througout the program
2. import pdb and use set_trace() which provides an interactive environment in the terminal to understand program flow
3. Create breakpoints in IDE's to create an interactive debugging environment

Try, except, else, finally

Try: A block of code where you anticipate errors, but would like to attempt execution
Except: A block of code to execute when a specific error happens
Else: A block of code that runs only if the try block executes successfully
Finally: A block of code that runs no matter what at the end
'''



'''
Two valueerrors that are giving the same error message.
We want two unique error messages for two different types of value errors.
How can we disginguish between these value errors? 
'''

