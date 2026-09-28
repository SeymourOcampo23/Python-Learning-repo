# Question 1 
name = "Seymour Ocampo"
print(name[0])
print(name[-1])
print(len(name))

string_1 = "Hello"
string_2 = "World"

print(string_1 + " " + string_2)

# # Question 2

text = "Python Programming"
# # First 6 characters
print(text[0:7])
# # Last 6 characters
print(text[-6:])
# # Every second character of the string
print(text[0::2])
# # Reverse the string
print(text[::-1])

# # String Methods and Functions
# # Question 3
# remove spaces in a string
text_2 = " i love python programming "
print(text_2)
print(text_2.strip())
# # Convert to titlecase
print(text_2.title())
# # Count how many times "o" appears
print(text_2.count("o"))

string_2 = "123abc"

print(string_2.isalnum())

# Question 4 String Formatting and f-Strings
# Using format() 
name = "John"
age = "25"
# Using f-strings
string_1 = "My name is {} and I am {} years old." 
print(string_1.format(name, age))

print(f"My name is {name} and I am {age} years old.")

# # Question 5 String Manipulation Challenges
sentence = "Coding in Python is fun" 

print(sentence.replace("fun","awesome"))  # Given sentence = "Coding in Python is fun" , replace "fun" with "awesome" and print it.

print(sentence.index("Python"))  # index of the word "Python" in sentence .

print(sentence.upper()) #Convert the entire sentence to uppercase and print it.

# # Bonus Question
# Take a user input string and check if it is a palindrome (same forwards and backwards)
word = (input("Enter a word: ")).lower()
if word == word[::-1]:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

# Write a program that counts how many vowels are in a given string.
word_2 = (input("Enter a word: ")).lower()
vowels = "aeiou"
sum = 0
for i in word_2:
    if i in vowels:
        sum = sum + 1
print(sum)

