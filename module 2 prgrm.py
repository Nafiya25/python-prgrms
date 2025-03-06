#1.Negative indexing in Python allows you to access elements from the end of a list. Instead of counting from the beginning (index 0), you count backward from the last element using negative numbers.(june 2022)

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print(fruits[-1])  
print(fruits[-2])  
print(fruits[-3])  

#2. Write a Python program to count how many times each character appears in a given string and store the count in a dictionary with key as the character.(june 2022)

def count_characters(string):
    char_count = {}  
    
    for char in string:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1
    return char_count


#3. Write a Python program to read n integers into a list and separate the positive and negative numbers into two different lists.(june 2022)

def separate_numbers(numbers):
    positive_numbers = []  
    negative_numbers = []  
    
    for num in numbers:
        if num >= 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)
    
    return positive_numbers, negative_numbers

n = int(input("Enter the number of integers: "))  
num_list = []

for _ in range(n):
    num = int(input("Enter a number: "))
    num_list.append(num)
positives, negatives = separate_numbers(num_list)
print("Positive numbers:", positives)
print("Negative numbers:", negatives)

#4.Create a dictionary of names and birthdays. Write a Python program that asks the user to enter a name, and the program display the birthday of that person. (2022)

birthdays = {
    "Alice": "March 12, 1995",
    "Bob": "July 8, 1992",
    "Charlie": "January 25, 1998",
    "David": "October 5, 1990"
}
name = input("Enter a name to find the birthday: ")
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print("Sorry, this name is not in the birthday list.")
    
#5.Write a Python code segment that opens a file for input and prints the number of 
four-letter words in the file.(2023)


def count_four_letter_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read() 
            words = text.split() 
            four_letter_words = [word for word in words if len(word) == 4]  
            print(f"Number of four-letter words: {len(four_letter_words)}")
    except FileNotFoundError:
        print("Error: File not found.")
# 6.Write a Python program to check whether a list contains a sublist. 
#  Eg. Input 1: my_list = [3,4,5,2,7,8] , sub_list = [2,7] 
#  output 1: True 
#  input 2: my_list = [3,4,5,2,7,8] , sub_list = [5,7] 
#  output 2: False (2023 may)

def contains_sublist(my_list, sub_list):
    return str(sub_list)[1:-1] in str(my_list)
my_list1 = [3, 4, 5, 2, 7, 8]
sub_list1 = [2, 7]
print(contains_sublist(my_list1, sub_list1))  # Output: True

my_list2 = [3, 4, 5, 2, 7, 8]
sub_list2 = [5, 7]
print(contains_sublist(my_list2, sub_list2))  # Output: False

# 7.Write a recursive function in python to find GCD of two numbers.(2023 may)

def gcd(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using recursion.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
#8.Assume that there is a text file named "numbers.txt" . Write a python program to find the median of list of numbers in the file without using standard function for median
#(June 2023)


 with open("numbers.txt", "r") as file:
    numbers = sorted(map(int, file.read().split()))

n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]  
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2 

print("Median:", median)


# 9. Use higher order python function filter to extract a list of positive numbers from a given list of numbers. You should use a lambda to create the auxiliary function .simple answers
# (June 2023)

 numbers = [-5, 3, -2, 8, 0, -1, 4]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

# 10.Write a Python program to compute the sum of the series (1- x
# 2
# /2! + x4
# /4! –
# x
# 6
# /6!+..........n terms).


import math

def series_sum(x, n):
    sum_series = 1 
    sign = -1 
    for i in range(2, 2 * n, 2):  
        term = (x ** i) / math.factorial(i)
        sum_series += sign * term
        sign *= -1 

    return sum_series

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
result = series_sum(x, n)
print("Sum of the series:", result)

# 11.Write a Python program to convert a decimal number to its binary equivalent.(Jan 2024)

def decimal_to_binary(n):
    return bin(n)[2:] 
num = int(input("Enter a decimal number: "))
print("Binary equivalent:", decimal_to_binary(num))
  
# 12.Write a Python program to read a text file and store the count of occurrences of 
# each character in a dictionary. (Jan 2024)


with open("textfile.txt", "r") as file:
    text = file.read()

char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
                                                
#13. Write a python program to create a list of squares for the numbers from 0 to 9 
# using list comprehension.
(May 2024)

squares = [x**2 for x in range(10)]
print(squares)

#14. Write a user-defined function to generate even numbers between 1 and 25(May 2024)

def even_numbers():
    return [x for x in range(1, 26) if x % 2 == 0]

print(even_numbers())


#15. Create a Python program that uses a dictionary to store the names and ages of 
# people. Ask the user to enter a name, and the program should display the age of 
# that person.
(May 2024)

people = {"Alice": 25, "Bob": 30, "Charlie": 22, "David": 28}
name = input("Enter a name: ")
age = people.get(name, "Name not found")
print("Age:", age)