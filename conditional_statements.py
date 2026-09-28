#If-Else Conditional Statements 
# Problem 1
num = int(input("Enter a number: "))
if num < 0:
    print("The number is negative.")
elif num > 0:
    print("The number is positive.")
else:
    print(f"The number is a {num}.")

#Problem 2
age = int(input("What is your age: "))

if age >= 18:
    print(f"You are {age} years old, you can vote")
elif age < 18:
    print(f"You are {age} 11 years old, you cannot vote.")

#Problem 3
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd. ")

#Match Case problems 
#problem 1
a = int(input("Enter a number: "))
match a:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")


#Problem 2
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
operator = (input("Enter an operator: "))

match operator:
    case "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    case "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    case "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    case "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")

#For Loop Conditional Problems

#Problem 1

for i in range (1, 11):
    print (i)

#Problem 2

num = int(input("Enter a number: "))
for i in range (1, 11):
    print(f"{num} * {i} = {num * i}")

# # Problem 3
sum = 0
for i in range (1, 101):
    sum = sum + i
print(sum)

#Problem 4
asterisks = "*"
for i in range (1, 5):
    print(asterisks)
    asterisks = asterisks + "*"

# While Loops Problems

# Problem 1
x = 1
while x <= 10:
    print(x)
    x += 1

# Problem 2
password = "Thbestmang23@"
is_false = True
while is_false:
    password_attempt = input("Enter your password: ")
    if password_attempt == password:
        print("You are now logging in...")
        is_false = False
    else:
        print("Wrong password, Try again.")
        continue


# Problem 3

num  = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse)

# Break, Continue, and Pass Statements

# Problem 1

for i in range (1, 11):
    if i == 7:
        break
    else:
        print(i)

# Problem 2
for i in range (1, 11):
    if i == 5:
        continue
    else:
        print(i)

# # Problem 3
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)

name = "SeymourOcampo"

reverse_firstname = name[6::-1]
print(reverse_firstname)

reverse_lastname = name[-1:6:-1]
print(reverse_lastname)