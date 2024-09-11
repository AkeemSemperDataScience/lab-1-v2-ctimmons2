def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb*1073741824
    return num_bytes

#answer = lab1Question1(1)
#print(answer)

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    m_length = len(name)
    if m_length > 0:
        is_odd = bool(m_length%2)
    else:
        return None
    return is_odd

#answer = lab1Question2('Colin')
#print(answer)
#answer = lab1Question2('Murray')
#print(answer)
#answer = lab1Question2('')
#print(answer)

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    if not input_string:
        character_at = -1
        return character_at
    if input_number <= len(input_string):
        character_at = input_string[input_number]
    else:
        character_at = -1
    return character_at

#answer = lab1Question3('Colin',2)
#print(answer)
#answer = lab1Question3('Colin',7)
#print(answer)

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    
    file1 = open(file_name,'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        
        list_of_nums.append(int(line.strip()))
        count += 1
    return list_of_nums

#answer = lab1Question4('github/test_file1.txt')
#print(answer)
#answer = lab1Question4('github/test_file2.txt')
#print(answer)

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    mode_of_list =  max(set(list_numbers), key = list_numbers.count)
 
    
    return mode_of_list

#listnumbers = [1, 2, 3, 3, 3, 3]
#answer = lab1Question5(listnumbers)
#print(answer)

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    calc = (quarters*.25)+(dimes*.1)+(nickels*.05)+(pennies*.01)
    #get a weird error in the debugger for (4,5,2,9) = 1.6900000000000002
    #so rounding to 2 decimal places and changing variables so not to change lab return statement
    total = round(calc, 2)
    return total


#answer = lab1Question6(4,3,2,1)
#print(answer)

## Example of calling a function to test these... 
# Question 1 Check:
#in_gb = 10
#expected_bytes = 10*1024*1024*1024
#calculated_bytes = lab1Question1(in_gb)

#print("Input gigabytes: ", in_gb)
#print("Expected bytes: ", expected_bytes)
#print("Calculated bytes: ", calculated_bytes)
#if expected_bytes == calculated_bytes:
#   print("Test passed")
#else:
#    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.